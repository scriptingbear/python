'''Emulate a simple library system according to the following specifications
1.) USER can DISPLAY all BOOKS in the LIBRARY
2.) USER can BORROW a BOOK from the LIBRARY
3.) System UPDATES itself when USER RETURNS one or more BOOKS

PLAN:
* Create Library class
* Create Book class
* Create Book Collection class
* Create Display(), Borrow(), Return() and Update() methods
* Persist library in file using pickle module
* Optional: Create Logger class


'''

'''PYBRARY CLASS
- Manages collection of Books
    - AddBook()
    - BorrowBook()
    - ReturnBook()
    - DisplayBooks() (filter/search?)

Data structure:
    - Dictionary
        -Keys are (fake) ISBN numbers of 13 digits (ex. 978-3-16-148410-0)
        -Items are lists consisting book object, followed by
         the current qty and then
         series of tuples [('mmddyyy', STATE)] showing transaction history
            -STATE is "B" (borrowed)
                "R" (returned)
                "A" (added)
                "D" (deleted-removed/destroyed)

        'sketch
        {NNNN:[book_obj, qty, ('mmddyyy', 'A'),  ('mmddyy', 'B'),
        ('mmddyyy', 'R')]

        NOTES:
            1st transaction is always 'A'
            Decrement qty for each 'B' transaction
            Increment qty for each 'R' transaction
            Current state of book is in last element of list

        Methods:
           -DisplayBooks() - print book name & author & qty on hand
           -BorrowBook() - append tuple to list; update qty
           -ReturnBook() - append tuple to list; update qty

'''

'''BOOK CLASS
     Has the following attributes:
     - ISBN
     - Title
     - Author
     - Pages
'''
#configure environment with modules needed for processing
import os, sys, re, pickle, datetime, enum

#create Book class, easiest task
class Book:
    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.ISBN = kwargs['ISBN']
        self.author = kwargs['author']
        self.pages = kwargs['pages']

#create enum for search type, to make code self documenting
class SearchType(enum.Enum):
    search_by_isbn = 1
    search_by_title = 2



#create Pybrary class, which houses the data structure
#only create one instance
class Pybrary:
    QTY_INDEX = 1
    PYBRARY_FILE = 'pybooks.txt'
    
    def __init__(self):
        self.dict_books = {}
        self.load_data()
 
    
    def load_data(self):
        if os.path.exists(self.PYBRARY_FILE):
            with open(self.PYBRARY_FILE, "rb") as libfile:
                self.dict_books = pickle.load(libfile)

    def save_data(self):
        if self.dict_books:
            with open(self.PYBRARY_FILE, "wb") as libfile:
                pickle.dump(self.dict_books, libfile)
                print("Data has been saved in file {}".format(self.PYBRARY_FILE))
        else:
            print("No books in pybrary database.")

    

    def getDateAsString(self):
        
        #get current date
        date_format_string = "{0:02d}{1:02d}{2:4d}"
        dt = datetime.datetime.now()
        date_as_string = date_format_string.format(dt.month, dt.day, dt.year)
        return date_as_string
        

    def addBook(self):
        #prompt user for book ISBN, title, author pages
        book_data = input("Enter book ISBN, Title, Author, " \
                          "# of Pages and quantity. Separate each item with an \"@\". " \
                          "Enter a blank to quit.: ")
        if not book_data:
            print("Program terminated.")
            return 
        
        #split input string and ensure it has 5 items
        book_data_parts = book_data.split('@')
        if len(book_data_parts) != 5:
            print("Invalid book data. Only {} out of 5 items provided." \
                  .format(len(book_data_parts)))
            return 
        else:
            #assign input to book data variables 
            book_isbn, book_title, book_author, book_pages, book_qty = book_data_parts
            
            #can't add a book that's already in the pybrary
            if self.dict_books.get(book_isbn):
                print("Book \"{0}\" (ISBN: {1}) already exists.". \
                      format(book_title, book_isbn))
            elif not book_qty.isnumeric():
                print("Invalid quantity")
                return
            elif int(book_qty) < 1:
                print("Quantity must be 1 or more")
                return
            
            
            #create new book object
            new_book = Book(ISBN=book_isbn, title=book_title,
                            author=book_author, pages=book_pages)

    
            #add a book to pybrary
            self.dict_books[new_book.ISBN] = [new_book, int(book_qty), (self.getDateAsString(), 'A')]
            print("Book \"{0}\" has been added. Current QTY is {1}". \
                       format(new_book.title, self.dict_books[new_book.ISBN][self.QTY_INDEX]))
        


    def findBook(self, search_term, search_type):
        #TODO: ISBN's are unique but titles aren't
        #may need to allow search based on both terms
        if search_type == SearchType.search_by_isbn:
            #find dictionary key
            #returns None if no matching key
            return self.dict_books.get(search_term)
            
        elif search_type == SearchType.search_by_title:
            #loop through dictionary, inspecting book object in
            #first element of list associated with each dictionary key
            #until a match is found
            for k,v in self.dict_books.items():
                if v[0].title == search_term:
                    return v
            #if no record matched the title, the following statement
            #will execute
            return None
        else:
            return None
            
    def borrowBook(self):
        #find by ISBN or Title
        search_term = input("Enter ISBN (starts with a digit) code or book title: ")
        if not search_term:
            print("ISBN or book title required.")
            return
        elif search_term[0].isnumeric():
            book_rec = self.findBook(search_term, SearchType.search_by_isbn)
        else:
            book_rec = self.findBook(search_term, SearchType.search_by_title)
            

        if not book_rec:
            print("Book not found.")
            return
        else:
            #add a tuple to the list associated with dictionary key that was found
            if book_rec[self.QTY_INDEX] >= 1:
                book_rec[self.QTY_INDEX] -=1
                book_rec.append((self.getDateAsString(), 'B'))
                book = book_rec[0]
                print("Book \"{0}\" has been borrowed. Current QTY is {1}". \
                       format(book.title, book_rec[self.QTY_INDEX]))
                
            else:
                print("No copies of this book are available currently.")
                

    def returnBook(self):
        #find by ISBN or Title
        search_term = input("Enter ISBN (starts with a digit) code or book title: ")
        if not search_term:
            print("ISBN or book title required.")
            return
        elif search_term[0].isnumeric():
            book_rec = self.findBook(search_term, SearchType.search_by_isbn)
        else:
            book_rec = self.findBook(search_term, SearchType.search_by_title)
            
        if not book_rec:
            print("Book not found.")
            return
        else:
            #only return book if last transaction was 'B'
            if book_rec[-1][1] != 'B':
                print("Cannot return book that isn't currently borrowed.")
                return
            
            #add a tuple to the list associated with dictionary key that was found
            book_rec[self.QTY_INDEX] +=1
            book_rec.append((self.getDateAsString(), 'R'))
            book = book_rec[0]
            print("Book \"{0}\" has been returned. Current QTY is {1}". \
                       format(book.title, book_rec[self.QTY_INDEX]))
                
        

    def DisplayBooks(self):
        if not self.dict_books:
            print("Pybrary is empty. No books to display.")
            return
        
        display_format = '{0:25} {1:25} {2:15} {3:12} {4:5} {5:3}'
        print(display_format.format('Title', 'Author', 'ISBN', 'Date', 'Status', ' QTY'))
        print('=' * 100)
        for k,v in self.dict_books.items():
            print(display_format.format(v[0].title, v[0].author, k, v[-1][0], v[-1][1], v[self.QTY_INDEX]))
            #print(v)
            




os.chdir(r'C:\Users\win2m\Documents\My Python Scripts')
#create library object
#it will load its data file, if one already exists
pylib = Pybrary()
print('Welcome to PYBRARY!!')

#create menu
menu = '''



Select option:
1.) Add book
2.) Borrow book
3.) Return book
4.) Display books
5.) Save data
Q.) Quit program
'''

#store function names in a list and invoke them by index
func_names = ['addBook', 'borrowBook', 'returnBook', 'DisplayBooks', 'save_data']

#display welcome message
while True:
    choice = input(menu)
    if not choice or choice == 'Q':
        #always try to save
        pylib.save_data()
        print("Program terminated.")
        break
    elif not choice.isnumeric():
        print("Invalid selection.")
        continue
    elif int(choice) not in range(1,6):
        print("Invalid selection.")
        continue
    else:
        getattr(pylib, func_names[int(choice)-1])()





                

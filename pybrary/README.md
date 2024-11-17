# pybrary
An exercise in Python 3 scripting where the task is to implement a very basic book management system

Here is my implementation of the coding challenge in which we are supposed to create a library management system. I think I may have over engineered. LOL But I was trying to translate the specification into a working, albeit *extremely* primitive application.

I originally wrote the code with the idea that there would be only 1 copy of each book. Some library, eh?! LOL But I modified it so that when a book is added the user can specify an amount. This allow for more testing scenarios. Still, the program doesn't track individual copies of each book.

The program will automatically save data using pickle into a file called pybooks.txt in the current working directory. It will load this file, if it exists, automatically when an instance of the Pybrary class is created.

The data structure is a dictionary object that follows this format:

{ISBN: [book_object, quantity, ('mmddyyy', status)....}

Each time a book is added, borrowed or returned an additional tuple is added to the list, as a sort of primitive audit trail.

I did not get around to implementing all of the features alluded to in my notes at the top of the file.

There are a lot of ways to crash this program or produce incorrect results. But I did spend several hours coding it and feel that I have learned a lot and had fun, too!

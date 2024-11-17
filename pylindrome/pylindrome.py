'''
Pylindrome: My take on determining if input is a pallindrome
First I solve the original challenge from testdome.com

Then I implement a new class called Pylindrome.
It works with strings, lists and dictionaries.
If it's a list. e.g. [1,2,3,2,1] it's a pylindrome if its elements
appear in a symmetrical sequence.

If it's a dictionary, every key must be a value and every value
must be a key in order to be considered a pylindrome

from testdome:

"A palindrome is a word that reads the same backward or forward.
Write a function that checks if a given word is a palindrome.
Character case should be ignored.
For example, is_palindrome("Deleveled") should return
True as character case should be ignored, resulting in "deleveled",
which is a palindrome since it reads the same backward and forward."
'''


#first solve original challenge
class Palindrome:

    @staticmethod
    def is_palindrome(word):
        if not word:
            return False
        else:
            word = word.lower()
            return word == word[::-1]

#test with original and my own data
items = ['Deleveled', 'hallucination', 'AbCDEdcBA', 'Level', 'rAcecaR', '']
for item in items:
    print('Is \"{}\" a palindrome? {}'.format(item, Palindrome.is_palindrome(item)))
    
print('\n' * 3)

#====================now for the fun part!====================================

class Pylindrome:

    @staticmethod
    def is_pylindrome(stuff):
        if not stuff:
            return False
        
        #what type of stuff is this?
        if type(stuff) is str:
            stuff = stuff.lower()
            return stuff == stuff[::-1]

        elif type(stuff) is list:
            #convert string elemements to lower
            temp = []
            
            for item in stuff:
                if type(item) is str:
                    temp.append(item.lower())
                else:
                    temp.append(item)

            stuff = temp
            return stuff[:(len(stuff)//2)+1] == stuff[(len(stuff)//2):][::-1]

        elif type(stuff) is dict:
            #values must be unique
            if len(set(stuff.values())) != len(stuff.values()):
                   return False
                   
            #every key must be a value
            for k in stuff.keys():
                if k not in stuff.values():
                   return False

            #every value must be a key
            for v in stuff.values():
                   if v not in stuff:
                       return False
            return True

        else:
            return False

#test Pylindrome!

items = ['AbCDEdcBA', {'oranges': 50, 'peaches': 20, 20: 'oranges', 50: 'peaches'}, [10,-50,'Python', True, 'Python',-50,10], \
         ['cat','dog','pArrot','bIrd','parrot','dOG','cat'], \
         [7,2,90,65,90,2,7], {'cat': 'meow', 'meow': 'cat', 'dog': 'bark', \
                              'wolf': 'howl', 'howl': 'dog', 'bark': 'wolf'}, \
         {'Dell': 400.50, 'Acer': 325.99, 'Toshiba': 1100.99, 400.50: 'Acer', \
          325.99: 'Dell', 1100.99: 'Toshiba'},
         {'a': 'b', 'b': 'd'}, [(1,2), (5,6), (1,2)], '', {}, []]

for item in items:
    print('Is \"{}\" a pylindrome? {}'.format(item, Pylindrome.is_pylindrome(item)))

'''
#====================================OUTPUT=============================================
Is "Deleveled" a palindrome? True
Is "hallucination" a palindrome? False
Is "AbCDEdcBA" a palindrome? True
Is "Level" a palindrome? True
Is "rAcecaR" a palindrome? True
Is "" a palindrome? False




Is "AbCDEdcBA" a pylindrome? True
Is "{'oranges': 50, 'peaches': 20, 20: 'oranges', 50: 'peaches'}" a pylindrome? True
Is "[10, -50, 'Python', True, 'Python', -50, 10]" a pylindrome? True
Is "['cat', 'dog', 'pArrot', 'bIrd', 'parrot', 'dOG', 'cat']" a pylindrome? True
Is "[7, 2, 90, 65, 90, 2, 7]" a pylindrome? True
Is "{'cat': 'meow', 'meow': 'cat', 'dog': 'bark', 'wolf': 'howl', 'howl': 'dog', 'bark': 'wolf'}" a pylindrome? True
Is "{'Dell': 400.5, 'Acer': 325.99, 'Toshiba': 1100.99, 400.5: 'Acer', 325.99: 'Dell', 1100.99: 'Toshiba'}" a pylindrome? True
Is "{'a': 'b', 'b': 'd'}" a pylindrome? False
Is "[(1, 2), (5, 6), (1, 2)]" a pylindrome? True
Is "" a pylindrome? False
Is "{}" a pylindrome? False
Is "[]" a pylindrome? False

'''


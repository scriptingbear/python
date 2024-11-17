# pylindrome
Pylindrome: My take on determining if input is a pallindrome
First I solve the original challenge from testdome.com

Then I implement a new class called Pylindrome.
It works with strings, lists and dictionaries.
If it's a list. e.g. [1,2,3,2,1] it's a pylindrome if its elements
appear in a symmetrical sequence.

If it's a dictionary, every key must be a value and every value
must be a key in order to be considered a pylindrome

from testdome:

A palindrome is a word that reads the same backward or forward.
Write a function that checks if a given word is a palindrome.
Character case should be ignored.
For example, is_palindrome("Deleveled") should return
True as character case should be ignored, resulting in "deleveled",
which is a palindrome since it reads the same backward and forward.

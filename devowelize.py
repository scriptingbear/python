# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

import sys, re

text = input("Enter some text from which vowels will be removed: ")
if not text:
    print("No text entered. Program terminated")
    sys.exit(-999)
elif  not re.compile(r'[aeiou]+').findall(text):
    print("Text does not contain any vowels. Program terminated")
    sys.exit(-999)

#create set of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
#create a set from the input string
text_set = set(text)
#subtract the vowels from the set derived from the input
text_set.difference_update(vowels)
if not text_set:
    print(sorted(list(text_set)))
else:
    print("You entered a string consisting of only vowels so there is nothing to return.")

    
    



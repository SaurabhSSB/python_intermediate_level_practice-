"""
Write a Python program to count repeated characters in a string.

	Sample string: 'thequickbrownfoxjumpsoverthelazydog'
	Expected output :
			o 4
			e 3
			u 2
			h 2
			r 2
			t 2

A program that prompts the user for a word and displays the character count of the word.
"""

str_1: str = input("Enter the string: ")
dict_1: dict = {}

for char in str_1:
    if char not in dict_1:
        dict_1[char]= 1
    else:
        dict_1[char]+= 1

for i in dict_1:
    if dict_1[i] > 1:
        print(i , dict_1[i])
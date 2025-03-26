"""
Program in python to find the number of vowels, consonants, digits, white space characters &
special characters in a string and save the result in the form of a dictionary.

For e.g.: Input: 'hello@123'
        Output: {'vowels':2, 'consonants':3, 'digits':3, 'whites':0, 'SpecChars':1}

A program that prompts the user for a string and displays the required information after traversing the string.
"""

word: str = input("Enter the string: ")
dict_1: dict = {"vowels": 0, "consonants": 0, "digits": 0, "whites": 0, "SpecChars": 0}

for i in word.lower():
    if i in {"a", "e", "i", "o", "u"}:
        dict_1["vowels"]+= 1
    elif i.isalpha():
        dict_1["consonants"]+= 1
    elif i.isdigit():
        dict_1["digits"]+= 1
    elif i.isspace():
        dict_1["whites"]+= 1
    else:
        dict_1["SpecChars"]+= 1

print(dict_1)
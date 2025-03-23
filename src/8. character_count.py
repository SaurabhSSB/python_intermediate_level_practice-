"""
Program in python to calculate the number of times a character is repeated in a given string.
Take the string and character from the user.

Example: Input String: "Neil Nitin Mukesh"
        Input Character: "e"
        Output: 2

A program that prompts the user for a string and a character and
displays the number of occurrence of that character.
"""

str_1: str = input("Enter the string: ")
chr_1: str = input("Enter character to be searched: ")

if len(chr_1) == 1:
    print(f"'{chr_1}' has {str_1.count(chr_1)} occurrences in {str_1}.")

else:
    print(f"{chr_1} is not acceptable. Please enter only one character.")
"""
Program in python to capitalize the first letter of the First Name and Surname
where whole name is taken as input from the user.

Example: Input: "first last" or "FIRST LAST" or "first lAst" i.e. Input can be in any case.
        Output: "First Last"

A program that prompts the user for a string and
displays the string after capitalizing the first letter of each word.
"""

str_1: str = input("Enter the string: ")

print(str_1.title())
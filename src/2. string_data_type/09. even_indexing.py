"""
Program in python which accepts string from the user and displays only those characters/elements
which are present at an even index.

Example:
    Input: "Python"
    Output: Pto

A program that prompts the user for input and
displays the character at even index.
"""

str_1: str = input("Enter string: ")

print(str_1[::2])
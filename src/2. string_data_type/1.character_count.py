"""
Program to count the number of each of the characters (character frequency)
in a string input by the user. Ignore the case.

For example: Input: "Python is great"
    Output: P = 1, y = 1, t = 2, and so on...

A program that prompts the user for a string and displays the character frequency.
"""

string: str = input("Enter a string: ")
d: dict = {}

for i in string.lower():
    if i in d:
        d[i]+= 1
    else:
        d[i]= 1

print(d)
"""
Program in python to generate and print a dictionary that contains a number (between 1 and n)
in the form {x : x*x} where n is the input from the user.

For e.g. Input: 4
        Output: {1:1, 2:4, 3:9, 4:16}

A program that prompts the user for a dictionary and
display the square series up till that number.
"""

num: int = int(input("Enter number: "))
dict_1: dict = {}

for i in range(1, num+1):
    dict_1[i]= i**2

print(dict_1)
"""
Program in python to compare two strings and tell the user if both of those strings are same or not.
Ignore their case.

Example: Input String1: "Hello"
	Input String2: "hello"
	Output: Strings are same

A program that prompts the user for two strings and displays whether they are same or not.
"""

str_1: str = input("Enter first string: ")
str_2: str = input("Enter second string: ")

if str_1.lower() == str_2.lower():
    print(f"{str_1} and {str_2} are same(ignoring case).")
else:
    print(f"{str_1} and {str_2} are not same.")
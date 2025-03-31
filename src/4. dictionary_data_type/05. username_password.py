"""
Program to save Username and Password of 10 employees in an organisation.
Take the Username and Password as input from the user one by one and save in the Dictionary.

A program that takes username and password from the user and form record using dictionary.
"""

dict_1: dict = {}
for i in range(10):
    dict_1[input(f"Enter the name of the {i+1}th employee.")]= input(f"Enter the password of {i+1}th employee.")

print(dict_1)
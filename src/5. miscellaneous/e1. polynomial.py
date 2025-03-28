"""
Program in python that accepts two integers (n) & (m) from user and
computes the value of 2n3 + 5m2 - 7n + 10

A program that prompts the user for two integers and displays a polynomial accordingly.
"""

num_1: int = int(input("Enter number: "))
num_2: int = int(input("Enter number: "))

print(2*num_1**3 + 5*num_2**2 - 7*num_1 +10)
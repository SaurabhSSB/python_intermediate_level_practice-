"""
Program in Python to find the Max of n numbers all taken as input from the user.

A program that prompts the user for multiple integer values and displays the biggest integer value.
"""

n: int = int(input("Enter the number of elements: "))

list_1: list = []

for i in range(n):
    list_1.append(int(input(f"Enter the {i+1}th number: ")))

print(max(list_1))
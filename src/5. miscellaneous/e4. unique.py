"""
Program which takes a sequence of numbers from the user and check if all input numbers are unique.

A program that takes a series of number as input and displays whether all the input numbers are unique or not.
"""

n: int = int(input("Enter the size of list: "))
li: list = []

for i in range(n):
    li+= input(f"Enter the {i+1}th element of the list.")

se: set = set(li)

print(f"The given list has all unique value is {len(se) == len(li)} statement.")
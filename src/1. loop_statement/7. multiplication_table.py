"""
WAP to print multiplication table of a number taken as input from the user.

For e.g. Input: 5
        Output: 5*1 = 5
                5*2 = 10
                .
                .
                .
                5*10 = 50

A program that prompts the user for an integer value and
display the multiplication table of that number.
"""

num: int = int(input("Enter number: "))

for i in range(1,11):
    print(f"{num} * {i} = {num * i}")

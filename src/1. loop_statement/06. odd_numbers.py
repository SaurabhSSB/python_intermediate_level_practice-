"""
WAP to print odd numbers in a given range in reverse order.
Take the range from the user as input.

For e.g. Input: start = 3
                End = 14
        Output: 13, 11, 9, 7, 5, 3

A program that prompts the user for two integer values and
displays a series of odd number between the range of the provided numbers in descending order.
"""

num_1: int = int(input("Enter number_1: "))
num_2: int = int(input("Enter number_2: "))

if num_1 < num_2:
    start: int = num_1
    end: int = num_2
else:
    start: int = num_2
    end: int = num_1

while start <= end:
    if end % 2 != 0:
        print(end, end= " ")
    end-= 1
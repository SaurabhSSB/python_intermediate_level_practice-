"""
WAP to print even numbers in a given range in reverse order.
Take the range from the user as input.

For e.g. Input: start = 3
                End = 14
        Output: 14, 12, 10, 8, 6, 4

A program that prompts the user for two inputs and
displays a series of even number between the range of two inputs in descending order.
"""

num_1: int = int(input("Enter number: "))
num_2: int = int(input("Enter number: "))

if num_1 < num_2:
    start: int = num_1
    end:   int = num_2

else:
    start: int = num_2
    end:   int = num_1

while start <= end:
    if end % 2 == 0:
        print(end, end= " ")
    end-= 1

"""
Write a python program to find the maximum and minimum number in a list of 10 elements
(taken as input from the user) and also find the index position of the these numbers.

   For example: Input : [25, 2, 1, 86, 42, 32, 27, 12, 31, 10]
		Output: Max Number: 86, Index of Max Number: 3
			Min Number: 1, Index of Min Number: 2

A program that prompts the user for 10 numbers and
displays maximum and minimum number with their indexes.
"""

li: list = []

for i in range(10):
    num_1: int = int(input(f"Enter {i+1}th number: "))
    li.append(num_1)

print(f"The maximum number is {max(li)} which is the {li.index(max(li)) + 1}th number.")
print(f"The minimum number is {min(li)} which is the {li.index(min(li)) + 1}th number.")

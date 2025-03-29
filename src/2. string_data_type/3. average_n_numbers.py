"""
Program in python to find average of n numbers taken as input from the user dynamically.

A program that prompts the user for numbers and displays the average of those numbers.
"""

n: int = int(input("Enter number: "))
total_sum: int = 0

for i in range(n):
    num: int = int(input(f"Enter {i+1}th number: "))
    total_sum+= num

print(f"The average is: {total_sum/n:.2f}.")
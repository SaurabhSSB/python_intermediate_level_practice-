"""
Accept n numbers from the user and display their average. n is input from the user.

For example:
    Input: n = 5
        Numbers = 3, 6, 2, 9, 0
    Output: Average = 4.0

A program that prompts the user to give a series of numbers and displays the average of those numbers.
"""

n: int = int(input("Enter the list size: "))
l: list = []

for i in range(n):
    i: float = float(input(f"Enter the {i+1}th number: "))
    l.append(i)

print(f"Average of given numbers is {sum(l)/len(l)}")
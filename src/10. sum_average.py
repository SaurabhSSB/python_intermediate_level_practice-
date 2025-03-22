"""
Program that keeps on accepting numbers from the user until the user enters Zero(0) as input.
Display the sum and average of all the numbers.

For example:
    Input: 3, 6, 8, 2, 5, Stop
    Output: Sum = 24
            Average = 4.8

A program that prompts the user for multiple numbers and then display their sum and average.
"""

x: bool = True
l: list = []

while x:
    n: str = input("Enter element: ")
    if n.isdigit():
        l.append(int(n))
        continue
    x= False


print(f"Sum of all the number provided is {sum(l)}")
print(f"Average of all the number provided is {sum(l)/len(l)}")
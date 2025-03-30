"""
Program to remove empty strings from the list of strings. Take list as input from the user.
For example: Input: ["My", "name", "", "is", "", "Alankrita", "", "."]
            Output: ["My", "name", "is", "Alankrita", "."]

A program that prompts the user for a series of string and
displays only non-empty strings.
"""

n: int = int(input("Enter the size of the list: "))
li: list = []

for i in range(n):
    lis: str = input(f"Enter the {i+1}th element: ")
    if lis != "":
        li.append(lis)

print(li)

"""
WAP to print all elements of a list using a for loop

A program that prompts the user for elements of list and
displays all the elements of the list in their respective data types.
"""

n: int = int(input("Enter the size of list: "))
l: list[str] = []

for i in range(n):
    x: str = input(f"Enter the {i+1}th element: ")
    if x.isdigit():
        l.append(int(x))
    else:
        l.append(x)

print(l)
"""
Program to remove/delete items from a list while iterating without creating a duplicate list.
Take the elements to be deleted from the user in real-time.

A program that prompts the user for a list of elements and then an element to remove and
display the list after removal.
"""

size: int = int(input("Enter the size of list: "))
li_1: list = []

for i in range(size):
    li_1.append(input(f"Enter the {i+1}th element: "))

rem_1: str = input("Enter the element to be removed: ")

li_1.remove(rem_1)

print(li_1)
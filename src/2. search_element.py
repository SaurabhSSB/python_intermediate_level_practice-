"""
WAP to take inputs from user to make a list. Length of the list has to be taken from the user.
Again take one input from user and search it in the list and delete that element, if found.
If not found, print "Element not present".

A program that prompts the user for list size and elements of list and a single variable,
then traverses the list and displays found if the element is found else not found.
"""

n: int = int(input("Enter element size: "))
l: list[str] = []

for i in range(n):
    x: str = input(f"Enter the {i+1}th element of the list: ")
    l.append(x)

l_search: str = input("Enter element to be searched: ")

if l_search in l:
    print(f"\n{l.index(l_search) + 1}th element in list is {l_search}.")
else:
    print(f"\n{l_search} not found in list.")
"""
Write a python program to find the intersection of elements from two list
(find the common elements in two lists).

A program that traverses through two lists and displays common elements.
"""

list_1: list = []
list_2: list = []
intersection_1: str= ""

n_1: int = int(input("Enter the length of list: "))
for i in range(n_1):
    list_1.append(input(f"Enter the {i+1}th element: "))

n_2: int = int(input("Enter the length of list_2: "))
for j in range(n_2):
    list_2.append(input(f"Enter the {j+1}th element: "))

for i in set(list_1):
    if i in set(list_2):
        intersection_1+= i

print(intersection_1)
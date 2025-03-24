"""
Program to concatenate two lists in the following order:
    list1 = ["Hello ", "World"]
    list2 = ["Hi", "There"]
    Output: ['Hello Hi', 'Hello There', 'World Hi', 'World There']

A program that prompts the user for two list and
displays the list in the required order.
"""

size: int = int(input("Enter size of the list: "))
li_1: list = []
li_2: list = []
li_3: list = []

for i in range(size):
    li_1.append(input(f"Enter the {i+1}th element of list 1: "))
    li_2.append(input(f"Enter the {i+1}th element of list 2: "))

for i in li_1:
    for j in li_2:
        li_3.append(i + " " + j)

print(li_3)
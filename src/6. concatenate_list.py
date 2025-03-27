"""
Program to concatenate two lists index-wise.
    list1 = ["M", "na", "i", "Ashu"]
    list2 = ["y", "me", "s", "tosh"]
    Output: ['My', 'name', 'is', 'Ashutosh']

A program that traverses two given list and displays a concatenated list.
"""

list1: list = ["M", "na", "i", "Ashu"]
list2: list = ["y", "me", "s", "tosh"]
list3: list = []

for i in range(len(list1)):
    list3.append(list1[i] + list2[i])

print(list3)
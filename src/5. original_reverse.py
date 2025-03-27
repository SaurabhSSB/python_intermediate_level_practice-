"""
Given two Python lists of same length. Iterate both lists simultaneously such that list1
should display item in original order and list2 in reverse order.

   For example: Input = list1 = [10, 20, 30, 40]
			list2 = [100, 200, 300, 400]
            Output: 10 400
                    20 300
                    30 200
                    40 100

A program that traverses through two given lists and
displays the list elements simultaneously one in original order and one in reverse.
"""

list1: list = [10, 20, 30, 40]
list2: list = [100, 200, 300, 400]

for i in range(len(list1)):
    print(list1[i], list2[-(i+1)],sep= " ")
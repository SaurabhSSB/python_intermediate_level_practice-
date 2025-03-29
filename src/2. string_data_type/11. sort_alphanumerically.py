"""
Write a Python program that accepts a comma separated sequence of words as input and
prints the unique words in sorted form (alphanumerically).

	Sample Words : red, white, black, red, green
	Expected Result : black, green, red, red, white

A program that prompts the user for a comma separated sequence of words and
displays a comma separated sequence in sorted order.
"""

str_1: str = input("Enter the string: ")

li_1: list = str_1.split(", ")
li_1.sort()

str_2: str = ", ".join(li_1)

print(str_2)
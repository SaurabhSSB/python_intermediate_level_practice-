"""
WAP to print the following pattern.
Here number_of_lines = 4. Take n as input from the user

1
1 2
1 2 3
1 2 3 4

A program that prompts the user for an integer value and
display pattern in accordance to the user input.
"""

num: int = int(input("Enter number of lines: "))

display: str= ""

for i in range(1, num+1):
    display+= str(i) +" "
    print(display)
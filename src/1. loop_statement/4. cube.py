"""
WAP to save the cube of all numbers from 1 to a number n in list,
where n is taken as input from the user.

For e.g. Input: 5
        Output: [1, 8, 27, 64, 125]  #Cube of numbers from 1 to 5 where 5 is the input from the user

A program that prompts the user of an integer value and
displays a list containing cube of all natural numbers up till that number.
"""

n: int = int(input("Enter number: "))
nc: list = []

if n<=0:
    print(f"{n} is not valid input.")
else:
    for i in range(1, n+1):
        nc.append(i ** 3)
    print(nc)
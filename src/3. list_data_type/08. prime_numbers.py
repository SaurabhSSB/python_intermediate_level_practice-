"""
Program to generate a Python list of all the prime numbers between n to m where n & m are taken as input from the user.

A program that prompts the user for two integers and displays a list of all prime number within that range.
"""

num_1: int = int(input("Enter number: "))
num_2: int = int(input("Enter number: "))
pl: list = []

if num_1 > num_2:
    start: int = num_2
    end: int = num_1

else:
    start: int = num_1
    end: int = num_2

while start <= end:
    prime: bool = True
    if start == 2 or start == 3:
        pl.append(start)
    elif start % 2 == 0 or start % 3 == 0:
        start += 1
        continue
    else:
        i = 5
        while i*i <= start:
            if start % i == 0 or start % i+2 == 0:
                prime = False
                break
            i+= 6
    if prime:
        pl.append(start)
    start+=1

print(pl)
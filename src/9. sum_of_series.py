"""
Write a program to calculate the sum of series up to n terms for a digit d.
n & d are taken as input from the user.

For example:
    Input: n = 5, d = 2
    Logic: 2 + 22 + 222 + 2222 + 22222
    Output: 24690


"""

n: int= int(input("Enter the number of terms wanted: "))
d: str= input("Enter the series wanted: ")
add: int= 0

for i in range(1, n+1):
    add+= int(d * i)

print(f"{n}th number of the series is {add}.")
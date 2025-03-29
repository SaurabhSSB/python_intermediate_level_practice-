"""
Program to find the digits which are absent in a given mobile number.

   For example: Input : 9354328855
                Output: 0167

A program that prompts the user for a mobile number and
after traversing displays the digits not present in input.
"""

mobile_no: str = input("Enter number: ")

for i in range(0, 10):
    if str(i) not in mobile_no:
        print(i, end= " ")
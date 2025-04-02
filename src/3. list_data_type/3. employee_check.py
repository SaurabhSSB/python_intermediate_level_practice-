"""
Program to check if a specific employee e is present in a company or not. Employee names are saved in a list.
e is taken as input from the user.

For example: empList = ["Ashwin", "Rachit", "Sanjana", "David", "Komal"]
            Input1: "Komal"
            Output1: "Employee is present"

            Input2: "Harshil"
            Output2: "Employee is not present"

A program that prompts the user for a name and
displays whether the name is present or not after traversing the list.
"""

empList: list = ["Ashwin", "Rachit", "Sanjana", "David", "Komal"]
name: str = input("Enter a name: ")

if name in empList:
    print(f"Employee {name} is present.")

else:
    print(f"Employee {name} is not present.")

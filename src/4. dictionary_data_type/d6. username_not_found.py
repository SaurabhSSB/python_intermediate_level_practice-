"""
Write an additional functionality to check if an employee is present in the organisation or not.
Basically "Search" Functionality based on their username
Take employee name as input from the user.
If the employee is present, print "Present" else print "Not Present"


"""

dict_1: dict = {}
for i in range(10):
    dict_1[input(f"Enter the name of the {i+1}th employee: ")]= input(f"Enter the password of {i+1}th employee: ")

name: str = input("Enter the name of the person to be searched: ")

if name in dict_1:
    print(f"Person {name} has {dict_1[name]} password.")
else:
    print(f"{name} is not present.")
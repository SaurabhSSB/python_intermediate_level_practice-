"""
Program to continuously take Names as input from the user.
Save the incoming names into a list as Full Name and save {First Name:Second Name} in a dictionary.
Take inputs till the user enters "Stop"

For e.g.: Input: "Shahrukh Khan", "Gauri Khan",..................."Stop"
         Output: list1 = ["Shahrukh Khan", "Gauri Khan",....................]
                 dict1 = {"Shahrukh":"Khan", "Gauri":"Khan", .....................}

A program that prompts the user for full name repeatedly and
displays output as dictionary with separate First and Second Name.
"""

x: bool = True
name: list[str] = []
name_separate :dict = {}

while x:
    name_1: str = input("Enter full name/Stop: ")
    if name_1.lower() == "stop":
        x= False
    else:
        name.append(name_1)

for names in name:
    separator= names.split(" ",1)
    name_separate[separator[0]]= separator[1]

print(name_separate)
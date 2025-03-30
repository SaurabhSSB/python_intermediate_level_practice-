"""
Given two lists having names of students and their corrsponding marks.
names = ["Ashutosh", "Ajay", "Alankrita", "Rachit", "Komal", "Anil"]
marks = [23, 21, 26, 23, 27, 24]
Take name of a student as input from the user and output his/her marks.

For e.g.:
    Input1: "Alankrita"
    Output1: 26

    Input2: "Someone"
    Output2: "Student not found"

A program that prompts the user for a name and displays their marks.
"""

names: list = ["Ashutosh", "Ajay", "Alankrita", "Rachit", "Komal", "Anil"]
marks: list = [23, 21, 26, 23, 27, 24]
name: str = input("Enter name: ")

if name in names:
    print(f"marks of {name} is {marks[names.index(name)]}.")
else:
    print("Student not found.")
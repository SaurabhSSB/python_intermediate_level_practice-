"""
Add an option to change marks of any students. Take student name and new marks from the user.
Print the modified list as output.

For e.g.: Input: "Ajay"
        new_mark: 25
        Output: marks = [23, 25, 26, 23, 27, 24]

A program that prompts the user for a name and marks and
displays list after updating that student info.
"""

names: list = ["Ashutosh", "Ajay", "Alankrita", "Rachit", "Komal", "Anil"]
marks: list = [23, 21, 26, 23, 27, 24]
name: str = input("Enter name: ")
mark: int = int(input("Enter student marks: "))

if name in names:
    marks[names.index(name)]= mark

else:
    names.append(name)
    marks.append(mark)

for i in range(len(names)):
    print(names[i]," - ",marks[i],"marks.")
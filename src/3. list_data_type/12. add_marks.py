"""
Give an option to enter the marks of a new student into the existing lists names and marks.
Take new data as input from user.
Print the new names and marks list as output.

For e.g.: Input: New_name = "Harshil"
                new_Marks = 20
        Output: names = ["Ashutosh", "Ajay", "Alankrita", "Rachit", "Komal", "Anil", "Harshil"]
                marks = [23, 21, 26, 23, 27, 24, 20]

A program that prompts the user for name and marks and
displays a list with the name added.
"""

names: list = ["Ashutosh", "Ajay", "Alankrita", "Rachit", "Komal", "Anil"]
marks: list = [23, 21, 26, 23, 27, 24]

name: str = input("Enter name: ")
mark: int = int(input("Enter marks: "))

if name in names:
    marks[names.index(name)]= mark
else:
    names.append(name)
    marks.append(mark)

for i in range(len(marks)):
    print(names[i]," - ",marks[i],"marks.")
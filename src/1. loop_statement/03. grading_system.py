"""
Make a grading system for a school based on the marks of the students using the following criteria.
Marks 0 - 40 : Grade F
     41 - 50 : Grade E
     51 - 70 : Grade D
     71 - 80 : Grade C
     81 - 90 : Grade B
     91 - 100: Grade A
Continuously take marks as input from the user and print the grade.
The user can enter "Stop" to stop the loop.

A program that prompts the user to enter
"""

x: bool = True

while x:
    num: int = int(input("Enter marks (0-100): "))
    if num > 90:
        print(f"{num} has Grade A.")
    elif num > 80:
        print(f"{num} has Grade B.")
    elif num > 70:
        print(f"{num} has Grade C.")
    elif num > 60:
        print(f"{num} has Grade D.")
    elif num > 50:
        print(f"{num} has Grade E.")
    else:
        print(f"{num} has Grade F.")

    x: str = input("Do you want to continue? (Continue/Stop): ")
    if x != "Continue":
        x= False
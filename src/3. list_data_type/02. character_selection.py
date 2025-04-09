"""
Program to make a list of all the characters starting from character 'A' to input character from the user.

For e.g. Input: 'H'
        Output: ["A", "B", "C", "D", "E", "F", "G", "H"]

A program that prompts the user for a character and
displays a list of alphabets up to that character.
"""

chr_1: str = input("Enter a character: ")
val_1: int = ord("A")
li_1: list = []

while val_1 <= ord(chr_1.upper()):
    li_1.append(chr(val_1))
    val_1+= 1

print(li_1)
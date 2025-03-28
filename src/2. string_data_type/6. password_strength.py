"""
Program in python to check the strength of the password input by the user based on the following features.
    Length minimum of 8 characters  (+1 Strength)
    Combination of upper case & lower case characters (+1 Strength)
    Combination of alphabets & digits (+1 Strength)
    Use of Special Characters (+1 Strength)

Example: Input: "Qwerty@123"
        Output: Strength = 4

A program that prompts the user for a string and displays it's strength as a password.
"""

password: str = input("Enter password: ")
strength: int = 0

if len(password) >= 8:
    strength+= 1
if any(c.isupper() for c in password) and any(c.islower() for c in password):
    strength+= 1
if any(c.isalpha() for c in password) and any(c.isdigit() for c in password):
    strength+= 1
if any(not c.isalnum() and  not c.isspace() for c in password):
    strength+= 1

print(f"Strength of '{password}' is {strength}.")
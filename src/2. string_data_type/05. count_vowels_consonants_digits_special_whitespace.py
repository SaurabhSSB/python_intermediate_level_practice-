"""
Program in python to find the number of vowels, consonants, digits, special
characters and white space characters in a string input by the user.

Example: Input: "Qwerty@123"
	output: v = 1, c = 5, d = 3, w = 0, s = 1

A program that prompts the user for a string and
displays vowel, consonant, digit, special character and white space character count.
"""

word: str = input("Enter the string: ")
v= c= d= w= s= 0

for i in word.lower():
    if i in {"a", "e", "i", "o", "u"}:
        v+= 1
    elif i.isalpha():
        c+= 1
    elif i.isdigit():
        d+= 1
    elif i.isspace():
        w+= 1
    else:
        s+= 1

print(f"No. of vowels:             {v}.")
print(f"No. of consonants:         {c}.")
print(f"No. of digits:             {d}.")
print(f"No. of whitespaces:        {w}.")
print(f"No. of special characters: {s}.")
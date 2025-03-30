"""
Program in python that accepts a hyphen-separated sequence of
words as input and prints the words in a hyphen-separated
sequence after sorting them alphabetically.

For e.g. Input: "p-y-t-h-o-n"
        Output: ['h', 'n','o', 'p', 't', 'y']

A program that prompts the user for hyphen separated sequence and
displays hyphen separated sequence after sorting.
"""

hseq: str = input("Enter a hyphen-separated sequence: ")
lhseq: list = hseq.split("-")

lhseq.sort()

print("-".join(lhseq))

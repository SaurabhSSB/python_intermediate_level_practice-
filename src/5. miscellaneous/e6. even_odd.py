"""
Program to take 10 integer inputs from the user and save them in a list.
The inputs have to be mix of even and odd numbers.
Now make one list to save all the even numbers from the input list.
Make another list for odd numbers too.

A program that prompts the user for 10 integer values and
displays two list by separating even and odd numbers.
"""

li_mix: list[int] = []
li_even: list[int] = []
li_odd: list[int] = []

for num in range(10):
    li_mix.append(int(input(f"Enter the {num + 1}th number: ")))

for eve_odd in li_mix:
    if eve_odd % 2 == 0:
        li_even.append(eve_odd)
    else:
        li_odd.append(eve_odd)

print(f"Even numbers are {li_even}.")
print(f"Odd numbers are {li_odd}.")
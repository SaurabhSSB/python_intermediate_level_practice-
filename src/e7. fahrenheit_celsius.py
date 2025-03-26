"""
Program to convert temperature in Fahrenheit to Celsius.
Take the temperature from the user in float type.

A program that prompts the user for Fahrenheit value and
display Celsius value.
"""

f: float = float(input("Enter Fahrenheit value: "))

print(f"Celsius value of {f} is {(f-32)*5/9:.2f}.")
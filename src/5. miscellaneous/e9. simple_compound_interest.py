"""
Program to make a simple and compound interest calculator. Take all the necessary data as input from the user.

A program that prompts the user for data and displays simple interest or compound interest accordingly.
SI= (P*T*R)/100
CI= P((1+(R/N)^(N*T) - 1)
"""

interest: str = input("Enter simple / compound: ")

if interest.lower()== "simple":
    p: float = float(input("Enter principal: "))
    t: float = float(input("Enter number of years: "))
    r: float = float(input("Enter rate: "))

    print(f"The total simple interest on {p:.2f} for time {t:.2f} and rate {r:.2f} is {(p*t*r)/100:.2f}.")

else:
    p: float = float(input("Enter principal: "))
    t: float = float(input("Enter number of years: "))
    r: float = float(input("Enter rate: "))
    n: float = float(input("Enter number of times interest compounded in a year: "))

    print(f"The total compound interest on {p:.2f} for time {t:.2f} and rate {r:.2f} is {p*(1+(r/n)**(n*t))-1:.2f}.")
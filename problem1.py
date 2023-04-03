#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution
# incorporate a while loop to keep having the user enter in values for a,b,c
# until they are valid
# incorporate a second while loop to keep repeating the program without
# having to rerun it.

""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')
while True:
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        break
    except ValueError:
        print("Invalid input. Please enter numerical coefficients only.")

while True:
    try:
        delta = b**2 - 4*a*c
        if delta < 0:
            raise ValueError("No real solutions.")
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        break
    except ValueError as error:
        print("Error:", error)
        print("Please enter new values for a, b, and c.")
        while True:
            try:
                a = float(input("Enter coefficient a: "))
                b = float(input("Enter coefficient b: "))
                c = float(input("Enter coefficient c: "))
                break
            except ValueError:
                print("Invalid input. Please enter numerical coefficients only.")

print("Solutions: x1 = {:.2f}, x2 = {:.2f}".format(x1, x2))

while True:
    repeat = input("Do you want to solve another quadratic equation? (y/n) ")
    if repeat.lower() == "n":
        break
    elif repeat.lower() == "y":
        while True:
            try:
                a = float(input("Enter coefficient a: "))
                b = float(input("Enter coefficient b: "))
                c = float(input("Enter coefficient c: "))
                break
            except ValueError:
                print("Invalid input. Please enter numerical coefficients only.")
        continue
    else:
        print("Invalid input. Please enter 'y' or 'n' only.")
        continue

print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")

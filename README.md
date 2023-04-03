## SDSS Computing Studies Python Assignment
### Assignment 017 Try Except Blocks

Objectives:
* Use try except to catch errors and work around them

https://www.w3schools.com/python/python_try_except.asp
'
When you are running a program and you generate an error, the program will stop and exit.  There are times when you might want to ignore the error and have the program keep going, or do something if an error pops up and use some alternate code.  In these cases, we use a try...except structure.  Many programs have this, although it is sometimes called try...catch.


Try...except is especially useful when you are asking the user to enter in a number, and they keep trying to enter in something with characters or symbols.  We could receive each keystroke, and check to see if the characters are valid keys, or we could just try to convert it, and if it doesn't work, throw an exception and ask them to do it again: example2.py

In example2.py, the **try** attempts to execute the code on lines 6 and 7.  If they are valid, then they are all kept. However, if the code is invalid, then the parts up to where the error occurred are kept, and everything below the error is ignored.

Try is a useful work around for when a program is not working correctly, but finding the solution to an error is going to take a lot of work.  It is not a substitute for good code in the long run.

## Task1
Retrieve numerical input

The following code will not work if the user enters in  invalid characters (ie non numerical characters) modify this code with a while loop along with a try...except block so that the user will keep entering in a number until they have entered a value integer value

## Task2
Reciprocal

Have the program iterate through the list and determine the reciprocal of each number as a decimal and print it. use the try/except to find any invalid values and display the error message

## Task 3
Square root of a number

Have the user enter in a number.  Use a try-except to see if the input is a valid number.  Determine the square root and use a try-except to catch exceptions if the number can not be square rooted note: Use the math.sqrt() function to determine a square root rather than number**(0.5) as we need to catch complex numbers as exceptions

## Problem 1
Quadratic Formula revisited

Have the user enter in the coefficients of a quadratic equation in the format: ax^2 + bx + c = 0 and calculate the solutions of the equation rounded to 2 decimal places. Use a try...except block to catch if there is no solution
* incorporate a while loop to keep having the user enter in values for a,b,c until they are valid
* incorporate a second while loop to keep repeating the program without having to rerun it.
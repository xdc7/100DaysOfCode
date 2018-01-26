"""
Write a function named collatz() that has one parameter named number. 
If number is even, then collatz() should print number // 2 and return this value. 
If number is odd, then collatz() should print and return 3 * number + 1.

Then write a program that lets the user type in an integer
 and that keeps calling collatz() on that number until the 
 function returns the value 1. 
 
"""

def collatz(number):
    if number % 2 == 0:
        print (number // 2)
        return (number // 2)
    else:
        print (3 * number + 1)
        return (3 * number + 1)
user_input = None
while True:
    try:
        print ("Please enter an integer")
        user_input = int(input())
    except ValueError:
        print ("Invalid number. Please try again")
        continue
    if user_input <= 0:
        print ("Please enter a positive number")
        continue
    break
while user_input is not None and True:
    user_input = collatz(user_input)
    if user_input == 1:
        break
        
        
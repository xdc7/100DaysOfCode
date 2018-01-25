"""
This game prompts a user to guess a number between 1 and 20 and then tries to guess the number
"""

import random
num = random.randint(1,20) # set the number to be guessed

counter = 1 # set the counter

#Ask the user for input and keep asking until they guess the correct number. Also record the number of tries

print ("I'm thinking of a number between 1 and 20. Can you guess it?")
while True:
    print ("Enter your guess and hit the Enter key: ")
    try:
        guess = int(input())
    except ValueError:
        print ("Invalid number. Please try again")
        continue
    counter += 1
    if guess == num:
        print("You guessed it!, The correct number is: %i and it took you %i attempts to guess it :)" % (num, counter))
        break
    elif guess < num:
        print ("You guessed too low. Please guess again...")
    elif guess > num:
        print ("You guess too high. Please guess again..")
    else:
        print ("I don't know how this condition could occur")
        
        
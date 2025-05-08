# Project 2: Guess the Number Game Python Project (Computer)

import random

def guess_the_number_computer():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    guess = 0
    while guess != number:
        guess = int(input("Guess the number: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct!")

guess_the_number_computer()

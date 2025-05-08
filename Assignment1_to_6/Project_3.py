# Project 3: Guess the Number Game Python Project (User)

def guess_the_number_user():
    print("Pick a number between 1 and 100 and think of it.")
    low, high = 1, 100
    while True:
        guess = (low + high) // 2
        response = input(f"Is your number {guess}? (y/n): ")
        if response == 'y':
            print("I guessed it!")
            break
        else:
            direction = input("Is it higher or lower? (h/l): ")
            if direction == 'h':
                low = guess + 1
            else:
                high = guess - 1

guess_the_number_user()

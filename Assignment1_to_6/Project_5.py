# Project 5: Hangman Python Project

def hangman():
    word = "python"
    guessed_letters = []
    attempts = 6
    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"Word: {display_word}")
        if display_word == word:
            print("You guessed the word!")
            break
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
    if attempts == 0:
        print(f"Game over! The word was {word}.")

hangman()

import random

NUM_ROUNDS = 5  # You can change this to play more or fewer rounds

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Extension 1: input safeguard
        while guess != "higher" and guess != "lower":
            guess = input("Please enter either higher or lower: ").lower()

        correct = False

        if guess == "higher" and user_number > computer_number:
            correct = True
        elif guess == "lower" and user_number < computer_number:
            correct = True

        if correct:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}\n")

    # Extension 2: Final message based on performance
    print("Thanks for playing!")
    print(f"Your final score was {score} out of {NUM_ROUNDS}")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()

import random

# This constant defines the likelihood of stopping.
DONE_LIKELIHOOD = 0.3  # Adjust this probability as desired

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():  # Call done() to see if we should stop
            return  # Exit the function if done() returns True
        print(curr_num)  # Print the current number if we haven't stopped

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()



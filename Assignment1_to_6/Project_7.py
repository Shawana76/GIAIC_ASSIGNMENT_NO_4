# Project 7: Password Generator Python Project

import random
import string

def password_generator():
    length = int(input("Enter password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print(f"Your password is: {password}")

password_generator()

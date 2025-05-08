MINIMUM_HEIGHT: int = 50  # Minimum height in arbitrary units

def tall_enough_extension():
    while True:
        user_input = input("How tall are you? (Press Enter to exit): ")
        if user_input.strip() == "":
            print("Goodbye! Have a great day! 🎉")
            break
        try:
            height = float(user_input)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tall_enough_extension()

if __name__ == '__main__':
    main()

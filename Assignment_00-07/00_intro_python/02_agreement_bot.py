def main():
    # Bold + Italic input prompt
    animal = input("\033[1;3mWhat's your favorite animal?\033[0m ")

    # Print user's favorite animal
    print(f"My favorite animal is also {animal}!")

if __name__ == "__main__":
    main()

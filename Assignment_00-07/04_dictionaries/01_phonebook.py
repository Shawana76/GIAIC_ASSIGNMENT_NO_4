def read_phone_numbers():
    """
    Ask the user to enter names and phone numbers to store in a phonebook.
    Return the phonebook dictionary.
    """
    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Print all names and their corresponding numbers from the phonebook.
    """
    print("\nPhonebook:")
    for name in phonebook:
        print(name + " -> " + phonebook[name])

def lookup_numbers(phonebook):
    """
    Allow the user to look up numbers by name.
    """
    print("\nLookup Numbers:")
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(name + "'s number is: " + phonebook[name])

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()

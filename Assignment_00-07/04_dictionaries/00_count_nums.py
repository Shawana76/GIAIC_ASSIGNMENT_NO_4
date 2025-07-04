def get_user_numbers():
    """
    Get numbers from the user until they enter a blank line.
    Return the list of numbers.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers

def count_nums(num_lst):
    """
    Count how many times each number appears in the list.
    Return a dictionary with numbers as keys and counts as values.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_counts(num_dict):
    """
    Print the number of times each number appeared.
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")

def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()

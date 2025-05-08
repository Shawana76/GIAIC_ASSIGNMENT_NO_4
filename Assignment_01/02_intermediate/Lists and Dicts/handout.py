def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range!"

def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return "Element updated successfully."
    else:
        return "Index out of range!"

def slice_list(my_list, start, end):
    if start < 0 or end > len(my_list):
        return "Start or end index out of range!"
    return my_list[start:end]

def play_index_game():
    my_list = ['car', 'book', 42, 'apple', 99]

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Show current list")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            try:
                index = int(input("Enter the index to access: "))
                print("Element at index", index, "is:", access_element(my_list, index))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == "2":
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                print(modify_element(my_list, index, new_value))
            except ValueError:
                print("Invalid input.")
        elif choice == "3":
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(my_list, start, end)
                print("Sliced list:", result)
            except ValueError:
                print("Invalid input. Please enter integers.")
        elif choice == "4":
            print("Current list:", my_list)
        elif choice == "5":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

if __name__ == "__main__":
    play_index_game()

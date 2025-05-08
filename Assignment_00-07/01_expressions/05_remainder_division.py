def main():
    try:
        # Get the numbers we want to divide
        dividend = int(input("Please enter an integer to be divided: "))
        divisor = int(input("Please enter an integer to divide by: "))

        quotient = dividend // divisor  # Integer division
        remainder = dividend % divisor  # Modulo operation
        
        print(f"The result of this division is {quotient} with a remainder of {remainder}")

    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid integers.")

if __name__ == '__main__':
    main()

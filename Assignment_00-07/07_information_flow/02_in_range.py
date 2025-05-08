def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if low <= n <= high:
        return True
    return False

def main():
    # Example usage of the in_range function
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    if in_range(n, low, high):
        print(f"{n} is in the range between {low} and {high}.")
    else:
        print(f"{n} is not in the range between {low} and {high}.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

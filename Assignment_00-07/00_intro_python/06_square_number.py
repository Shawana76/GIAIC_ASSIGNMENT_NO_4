def main():
    number = float(input("\033[1;3mType a number to see its square:\033[0m "))
    
    square = number * number

    print(f"The square of {number} is {square}")

if __name__ == '__main__':
    main()

import math

def main():
    ab = float(input("Enter the length of side AB: "))
    bc = float(input("Enter the length of side BC: "))

    ac = math.sqrt(ab**2 + bc**2)

    print(f"The length of the hypotenuse (AC) is {ac:.2f}")

if __name__ == '__main__':
    main()

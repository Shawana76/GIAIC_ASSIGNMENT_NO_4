def main():
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    perimeter = side1 + side2 + side3

    print(f"\n🔺 The perimeter of the triangle is: {perimeter:.2f}")
    

if __name__ == '__main__':
    main()

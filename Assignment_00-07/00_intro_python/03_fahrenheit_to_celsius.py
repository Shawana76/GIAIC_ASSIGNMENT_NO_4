def main():
    # Input with bold + italic style
    fahrenheit = float(input("\033[1;3mEnter temperature in Fahrenheit:\033[0m "))

    # Convert to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Print result
    print(f"Temperature: {fahrenheit}°F = {celsius:.2f}°C")

if __name__ == "__main__":
    main()

"""
Prompts the user for a weight on Earth
and a planet. Then prints the equivalent
weight on that planet. Case-insensitive and 
handles invalid inputs gracefully.
"""

# Gravitational constants relative to Earth
GRAVITY_CONSTANTS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Earth": 1.0,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    try:
        # Get Earth weight from the user
        earth_weight = float(input("Enter a weight on Earth: "))

        # Get planet name and format it properly
        planet = input("Enter a planet: ").strip().capitalize()

        if planet in GRAVITY_CONSTANTS:
            gravity_constant = GRAVITY_CONSTANTS[planet]
            planetary_weight = round(earth_weight * gravity_constant, 2)
            print(f"The equivalent weight on {planet}: {planetary_weight}")
        else:
            print("Invalid planet name. Please enter a valid planet like Mars, Jupiter, etc.")
    except ValueError:
        print("Please enter a valid number for weight.")

if __name__ == "__main__":
    main()

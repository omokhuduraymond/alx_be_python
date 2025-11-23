FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        try:
            choice = float(input("Enter the temperature to convert: "))
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.\n")
            continue

        pace = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if pace == 'C':
            converted = convert_to_fahrenheit(choice)
            print(f"{choice}°C is {converted:.2f}°F")
        elif pace == 'F':
            converted = convert_to_celsius(choice)
            print(f"{choice}°F is {converted:.2f}°C")
        else:
            print("INVALID INPUT. Please enter C or F.\n")

if __name__ == "__main__":
    main()
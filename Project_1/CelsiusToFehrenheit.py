# Fahrenheit to Celsius
print("--- Fahrenheit to Celsius ---")
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Formula: C = (F - 32) * 5/9
celsius = (fahrenheit - 32) * 5/9

print(f"The given fahrenheit is {fahrenheit:.2f}°F is equal to {celsius:.2f}°C celsius\n")


# --- Celsius to Fahrenheit
print("--- Celsius to Fahrenheit ---")
fahrenheit = float(input("Enter temperature in Celsius: "))

# Formula: F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

print(f"the given celcius is {celsius:.2f}°C is equal to {fahrenheit:.2f}°F fahrenheit")
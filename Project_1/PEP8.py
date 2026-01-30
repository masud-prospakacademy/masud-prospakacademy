
celsius_string = input("Enter temperature in Celsius: ")


celsius_float = float(celsius_string)


fahrenheit_result = (celsius_float * 9/5) + 32

print(f"The given celsius is {celsius_float}C, and the fahrenhiet is {fahrenheit_result:.2f}F")

name = input("Enter your name: ")

age = int(input("Enter your age: "))

height_cm = float(input("Enter your height in centimeters: "))

is_student = input("Are you a student? (Type 'True' or 'False'): ")

# Convert Height to Inches
# Formula: inches = centimeters / 2.54
height_inches = height_cm / 2.54

print("\n" + "-" * 10 + " User Profile " + "-" * 10)
print(f"Name:           {name}")
print(f"Age:            {age} years old")
print(f"Student Status: {is_student}")
print(f"Height:         {height_cm} cm ({height_inches:.2f} inches)")
print("-" * 34)
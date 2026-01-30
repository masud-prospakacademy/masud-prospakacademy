def safe_divide(): 
    print("\n--- Safe Division Calculator ---") 
    try: 
        num1 = float(input("Enter the numerator: ")) 
        num2 = float(input("Enter the denominator: ")) 
 
        result = num1 / num2 
 
    except ZeroDivisionError: 
        print("Error: You cannot divide by zero!") 
        
    except ValueError: 
        print("Error: Invalid input. Please enter valid numbers.") 
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    else: 
        print(f"Result: {result}") 
 
    finally: 
        print("Calculation attempt complete.")

safe_divide()
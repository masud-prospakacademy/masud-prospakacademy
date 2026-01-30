
import random

secret_number = random.randint(1, 100)

num_guesses = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    user_guess_str = input("Guess the number (1-100): ")
    user_guess = int(user_guess_str)
    
    num_guesses += 1
    
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {num_guesses} attempts!")
        break  
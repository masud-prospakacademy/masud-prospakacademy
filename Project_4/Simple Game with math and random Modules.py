import random
import math

def start_game():
    secret_number = random.randint(1, 100)
    max_guesses = 7
    guesses_taken = 0
    last_guess = None

    print("\n" + "="*30)
    print("WELCOME TO THE ENHANCED GUESSER")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_guesses} attempts. Type 'hint' if you're stuck!")
    print("="*30)

    while guesses_taken < max_guesses:
        guess_str = input(f"\n[Attempt {guesses_taken + 1}/{max_guesses}] Enter your guess: ").strip().lower()

        if guess_str == "hint":
            if last_guess is None:
                print("You need to make at least one numeric guess before asking for a contextual hint!")
            else:
                if last_guess < secret_number:
                    hints = ["It's higher than your last guess!", "Try adding 10 to your previous guess.", "Look toward the upper end of the range."]
                else:
                    hints = ["It's lower than your last guess!", "Try subtracting 5 from your previous guess.", "Look toward the lower end of the range."]
                print(f"HINT: {random.choice(hints)}")
            continue

        try:
            guess = int(guess_str)
        except ValueError:
            print("Invalid input! Please enter a whole number or 'hint'.")
            continue

        guesses_taken += 1
        last_guess = guess

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {guesses_taken} attempts!")
            return True 

        if guesses_taken >= 3 and guesses_taken < max_guesses:
            sqrt_hint = math.floor(math.sqrt(secret_number))
            print(f"MATH HINT: The integer part of the square root of the secret number is {sqrt_hint}.")

    print(f"\nGame Over! You ran out of guesses. The number was {secret_number}.")
    return False

if __name__ == "__main__":
    start_game()
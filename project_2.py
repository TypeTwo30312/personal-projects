"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bulls & Cows

author: Tomáš Vamberský

email: tomas.vambersky@protonmail.com

discord: typetwo

"""

import random

def generate_secret_number():
    """Generates a random 4-digit number (no repeats, no leading zero)."""
    digits = list("0123456789")
    while True:
        secret = random.sample(digits, 4)
        if secret[0] != "0":
            return "".join(secret)
        
def is_valid_guess(guess):
    """Evaluates the guess"""
    if not guess.isdigit():
        print("Please enter digits only.")
        return False
    if len(guess) != 4:
        print("The number must be exactly 4 digits long.")
        return False
    if guess[0] == "0":
        print("The number cannot start with zero.")
        return False
    if len(set(guess)) != 4:
        print("Digits must not repeat.")
        return False
    return True

def count_bulls_and_cows(secret, guess):
    """Return the number of bulls and cows for a given guess."""
    bulls = sum(1 for i in range(4) if guess[i] == secret[i])
    cows = sum(1 for char in guess if char in secret) - bulls
    return bulls, cows

def evaluate_skill(attempts):
    """Return a comment on the player's performance based on number of attempts."""
    if attempts <= 7:
        return "Excellent! You really know how to play!"
    elif attempts <= 12:
        return "Good job! That's a solid result."
    elif attempts <= 20:
        return "Not bad, but there's room for improvement."
    else:
        return "Keep practicing! Try to use elimination and strategy."

def play_game():
    """Main game loop."""
    secret = generate_secret_number()
    attempts = 0
    print("""
Hi there!
-----------------------------------------------
I've generated a random 4-digit number for you.
Let's play a Bulls and Cows game.
-----------------------------------------------
""")
    while True:
        guess = input("Enter your guess: ")
        print("-----------------------")
        if not is_valid_guess(guess):
            continue

        attempts += 1
        bulls, cows = count_bulls_and_cows(secret, guess)
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        print("-----------------------")
        if bulls == 4:
            print(f"Correct!!! You guessed the secret number in {attempts} guesses.")
            print(evaluate_skill(attempts))
            break
    
if __name__ == "__main__":
    play_game()
"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bulls & Cows

author: Tomáš Vamberský

email: tomas.vambersky@protonmail.com

discord:

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

secret_number = "1234"
print(count_bulls_and_cows(secret_number, "3245"))
print(generate_secret_number())
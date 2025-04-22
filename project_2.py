"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bulls & Cows

author: Tomáš Vamberský

email: tomas.vambersky@protonmail.com

discord:

"""

import random

def generate_secret_number():
    """Generate a random 4-digit number (no repeats, no leading zero)."""
    digits = list("0123456789")
    while True:
        secret = random.sample(digits, 4)
        if secret[0] != "0":
            return "".join(secret)
        
print(generate_secret_number())
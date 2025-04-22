"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Vamberský

email: tomas.vambersky@protonmail.com

discord:

"""
import sys

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = {1: "Situated about 10 miles west of Kemmerer, "
"Fossil Butte is a ruggedly impressive"
"topographic feature that rises sharply"
"some 1000 feet above Twin Creek Valley"
"to an elevation of more than 7500 feet"
"above sea level. The butte is located just"
"north of US 30N and the Union Pacific Railroad,"
"which traverse the valley. ", 
         2: "Pokud uživatel vybere takové číslo textu,"
         " které není v zadání, program jej upozorní a skončí",
         3: "The monument contains 8198 acres and protects"
         "a portion of the largest deposit of freshwater fish"
         "fossils in the world. The richest fossil fish deposits"
         "are found in multiple limestone layers, which lie some"
         "100 feet below the top of the butte. The fossils"
         "represent several varieties of perch, as well as"
         "other freshwater genera and herring similar to those"
         "in modern oceans. Other fish such as paddlefish,"
         "garpike and stingray are also present."
         }

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in users and users[username] == password:
    print("Login successful!")
    print("We have 3 texts to be analyzed.")
    
    try:
        number = int(input("Enter a number between 1 - 3 to select text: "))
    except ValueError:
        print("Entered value is not a number, terminating.")
        sys.exit()
    if number not in TEXTS:
        print("Entered value is not one of the available numbers, terminating")
        sys.exit()
    text = (TEXTS.get(number))
    words = text.split()
    print(len(words))

else:
    print("Invalid username or password.")
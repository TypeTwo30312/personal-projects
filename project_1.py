"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Vamberský

email: tomas.vambersky@protonmail.com

discord: TypeTwo

"""
import sys
import string

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = {
    1: "Situated about 10 miles west of Kemmerer, "
        "Fossil Butte is a ruggedly impressive "
        "topographic feature that rises sharply "
        "some 1000 feet above Twin Creek Valley "
        "to an elevation of more than 7500 feet "
        "above sea level. The butte is located just "
        "north of US 30N and the Union Pacific Railroad, "
        "which traverse the valley. ", 
    2: "At the base of Fossil Butte are the bright "
        "red, purple, yellow and gray beds of the Wasatch "
        "Formation. Eroded portions of these horizontal "
        "beds slope gradually upward from the valley floor "
        "and steepen abruptly. Overlying them and extending "
        "to the top of the butte are the much steeper "
        "buff-to-white beds of the Green River Formation, "
        "which are about 300 feet thick.",
    3: "The monument contains 8198 acres and protects "
        "a portion of the largest deposit of freshwater fish "
        "fossils in the world. The richest fossil fish deposits "
        "are found in multiple limestone layers, which lie some "
        "100 feet below the top of the butte. The fossils "
        "represent several varieties of perch, as well as "
        "other freshwater genera and herring similar to those "
        "in modern oceans. Other fish such as paddlefish, "
        "garpike and stingray are also present."
         }

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in users and users[username] == password:
    print("Login successful!")
    print("---------------------------------")
    print("We have 3 texts to be analyzed.")
    print("---------------------------------")
    try:
        number = int(input("Enter a number between 1 - 3 to select text: "))
    except ValueError:
        print("Entered value is not a number, terminating.")
        sys.exit()
    if number not in TEXTS:
        print("Entered value is not one of the available numbers, terminating")
        sys.exit()
    text = (TEXTS.get(number))
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    word_length_count = {}
    for word in words:
        if not word.isdigit(): ### This excludes numbers from word counts
            length = len(word)
            if length in word_length_count:
                word_length_count[length] += 1
            else:
                word_length_count[length] = 1
    max_count = max(word_length_count.values())

    print("---------------------------------")
    print(f"There are {len(words)} words in the selected text, of which {sum(1 for word in words if not word.isdigit())} are not numbers.")
    print(f"There are {sum(1 for word in words if word.istitle())} titlecase words.")
    print(f"There are {sum(1 for word in words if word.isupper())} uppercase words.")
    print(f"There are {sum(1 for word in words if word.islower())} lowercase words.")
    print(f"There are {sum(1 for word in words if word.isdigit())} numeric strings.")
    print(f"The sum of all the numbers {sum(int(word) for word in words if word.isdigit())}")
    print("---------------------------------")

    print(f"LEN | ocurrence {' '*(max_count-9)} | number")
    print("---------------------------------")
    for length in sorted(word_length_count):
        count = word_length_count[length]
        print(f"{str(length).rjust(3)} | {'*' * count} {' '*(max_count-count)} | {count}")

else:
    print("Invalid username or password.")
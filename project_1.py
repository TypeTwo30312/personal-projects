"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Vamberský

email: tomas.vambersky@protonmail.com

discord:

"""
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid username or password.")
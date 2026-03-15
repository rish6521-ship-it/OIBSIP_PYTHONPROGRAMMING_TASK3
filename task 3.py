import random
import string

print("----- Password Generator -----")

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Ask user for character preferences
use_letters = input("Include letters? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

characters = ""

# Add character sets based on user choice
if use_letters == 'y':
    characters += string.ascii_letters
if use_numbers == 'y':
    characters += string.digits
if use_symbols == 'y':
    characters += string.punctuation

# Check if at least one option is selected
if characters == "":
    print("Error: You must select at least one character type!")
else:
    password = ""
    
    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""

    if use_letters:
        characters += string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Secure Password Generator ===")

    length = int(input("Enter password length: "))

    letters = input("Include letters? (y/n): ").lower() == "y"
    numbers = input("Include numbers? (y/n): ").lower() == "y"
    symbols = input("Include special characters? (y/n): ").lower() == "y"

    password = generate_password(length, letters, numbers, symbols)

    print("\nGenerated Password:", password)


if __name__ == "__main__":
    main()
import random
import string
import studentutils as su


def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def save_password(password, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(password + "\n")


if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    password = generate_password(
        length, use_uppercase, use_numbers, use_special)
    print("Generated Password:", password)
    save_password(password)
    print("Password saved to passwords.txt")

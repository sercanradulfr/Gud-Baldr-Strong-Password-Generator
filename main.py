import random
import string
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Gud Baldr")
print(ascii_banner)

def generate_password(length=12):
    """
    Generate a random password of specified length.
    By default, it generates a 12-character password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)
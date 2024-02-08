import random
import string

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + "_@&-!%$#?"
    password = ''.join(random.choice(characters) for i in range(length))
    return print(password)

generate_password(length=15)
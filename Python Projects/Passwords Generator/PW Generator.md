# Python Password Generator  

**Usage:**

1. Clone or download the script to your local machine.
2. Run the script using a Python interpreter.
   
   ```bash
   python password_generator.py
   ```
4. You can also specify the length of the password you want by passing the desired length to the `generate_password` function.
   ```python
   generate_password(length=15)
   ```

---

**Code:**

```python
import random
import string

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + "_@&-!%$#?"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_password(length=15))  # Output: Randomly generated password
```

The `generate_password` function generates a password of the specified length. By default, it generates a password of length 12. It includes uppercase and lowercase letters, digits, and special characters such as "_@&-!%$#?".

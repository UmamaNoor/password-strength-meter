import re
import random
import string

def check_password_strength(password):
    """Checks the strength of a password and returns a rating."""
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])

    if score == 5:
        return "Strong 💪"
    elif score >= 3:
        return "Medium 😐"
    else:
        return "Weak ❌"
    
def generate_password(length=12):
    """Generates a secure random password of a given length."""
    if length < 8:
        print("Warning: It's recommended to use a password of at least 8 characters!")
    
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

# Example usage
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    print(f"Password Strength: {check_password_strength(user_password)}")

    new_password = generate_password(12)
    print(f"Generated Secure Password: {new_password}")

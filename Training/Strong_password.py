import random
import string

# Extended substitution map for a–z
sub_map = {
    'a': ['@', '4'], 'b': ['8'], 'c': ['(', '<'], 'd': ['|)', 'cl'],
    'e': ['3'], 'f': ['ph'], 'g': ['6', '9'], 'h': ['#'], 'i': ['1', '!'],
    'j': ['_|'], 'k': ['|<'], 'l': ['1', '|'], 'm': ['^^', '/\\/\\'],
    'n': ['^/', '/\\/'], 'o': ['0'], 'p': ['|*'], 'q': ['(,)'],
    'r': ['|2'], 's': ['5', '$'], 't': ['7', '+'], 'u': ['(_)'],
    'v': ['\\/'], 'w': ['\\/\\/'], 'x': ['%', '><'], 'y': ['`/'],
    'z': ['2']
}

def substitute_chars(password, substitution_rate=0.6):
    new_password = ''
    for char in password:
        lower_char = char.lower()
        if lower_char in sub_map and random.random() < substitution_rate:
            new_password += random.choice(sub_map[lower_char])
        else:
            new_password += char
    return new_password

def strengthen_password(password, min_length=12):
    # Step 1: Substitute characters
    password = substitute_chars(password)

    # Step 2: Ensure diversity
    if not any(c.islower() for c in password):
        password += random.choice(string.ascii_lowercase)
    if not any(c.isupper() for c in password):
        password += random.choice(string.ascii_uppercase)
    if not any(c.isdigit() for c in password):
        password += random.choice(string.digits)
    if not any(c in string.punctuation for c in password):
        password += random.choice(string.punctuation)

    # Step 3: Pad to minimum length
    while len(password) < min_length:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    # Step 4: Shuffle for randomness
    password = ''.join(random.sample(password, len(password)))
    return password

# Example usage
user_input = input("Enter your password: ")
strong_password = strengthen_password(user_input)
print("Strengthened password:", strong_password)
import random
import string

def generate_password(length):
    # Ensure the password length is at least 4 to accommodate all character types
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to include all required character types.")

    # Define the required characters
    uppercase_letter = random.choice(string.ascii_uppercase)
    lowercase_letter = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special_character = random.choice('#@*')

    # Generate the remaining characters randomly
    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + '#@*'
    remaining_characters = ''.join(random.choice(all_characters) for _ in range(remaining_length))

    # Combine all parts
    password_list = list(uppercase_letter + lowercase_letter + digit + special_character + remaining_characters)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def main():
    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Generate the password
    try:
        password = generate_password(length)
        # Display the generated password
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

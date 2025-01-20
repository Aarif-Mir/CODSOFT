import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_characters = string.punctuation

    def get_user_preferences(self):
        print("Welcome to the Password Generator!")
        try:
            length = int(input("Enter the desired password length (minimum 6): "))
            if length < 6:
                raise ValueError("Password length must be at least 6.")
            include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
            include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
            include_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
            
            return length, include_uppercase, include_digits, include_special
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def generate_password(self, length, include_uppercase, include_digits, include_special):
        # Combine character pools based on preferences
        pool = self.lowercase
        if include_uppercase:
            pool += self.uppercase
        if include_digits:
            pool += self.digits
        if include_special:
            pool += self.special_characters

        if not pool:
            raise ValueError("At least one character type must be selected!")

        # Generate password
        return ''.join(random.choice(pool) for _ in range(length))

    def run(self):
        while True:
            preferences = self.get_user_preferences()
            if preferences:
                length, include_uppercase, include_digits, include_special = preferences
                try:
                    password = self.generate_password(length, include_uppercase, include_digits, include_special)
                    print(f"Your generated password is: {password}")
                except ValueError as e:
                    print(f"Error: {e}")

            # Ask if user wants to generate another password
            retry = input("Generate another password? (yes/no): ").strip().lower()
            if retry != 'yes':
                print("Thank you for using the Password Generator!")
                break


if __name__ == "__main__":
    app = PasswordGenerator()
    app.run()

import re


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    @staticmethod
    def validate_phone(phone):
        if re.fullmatch(r"\d{10}", phone):
            return True
        print("Invalid phone number! It must be a 10-digit number.")
        return False

    @staticmethod
    def validate_email(email):
        if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        print("Invalid email format! Please provide a valid email address (e.g., example@gmail.com).")
        return False

    @staticmethod
    def validate_input(prompt, validation_function):
        while True:
            user_input = input(prompt).strip()
            if user_input and validation_function(user_input):
                return user_input
            print("This field is required and must be valid. Please try again.")

    def add_contact(self):
        print("Add a New Contact:")
        name = input("Enter Name: ").strip()
        if not name:
            print("Name is required!")
            return
        phone = self.validate_input("Enter Phone Number: ", self.validate_phone)
        email = self.validate_input("Enter Email: ", self.validate_email)
        address = input("Enter Address: ").strip()
        if not address:
            print("Address is required!")
            return
        self.contacts.append(Contact(name, phone, email, address))
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found!")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if not results:
            print("No matching contacts found!")
        else:
            for contact in results:
                print(contact)

    def update_contact(self, query):
        for contact in self.contacts:
            if query.lower() == contact.name.lower() or query == contact.phone:
                print("Contact found!")
                print(contact)
                print("\nEnter new details (leave blank to keep unchanged):")
                name = input(f"New Name [{contact.name}]: ").strip() or contact.name
                phone = self.validate_input("New Phone Number (leave blank to skip): ", self.validate_phone) or contact.phone
                email = self.validate_input("New Email (leave blank to skip): ", self.validate_email) or contact.email
                address = input(f"New Address [{contact.address}]: ").strip() or contact.address
                contact.name, contact.phone, contact.email, contact.address = name, phone, email, address
                print(f"Contact '{name}' updated successfully!")
                return
        print("Contact not found!")

    def delete_contact(self, query):
        for contact in self.contacts:
            if query.lower() == contact.name.lower() or query == contact.phone:
                self.contacts.remove(contact)
                print(f"Contact '{contact.name}' deleted successfully!")
                return
        print("Contact not found!")

    def run(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            try:
                choice = int(input("Choose an option: "))
                if choice == 1:
                    self.add_contact()
                elif choice == 2:
                    self.view_contacts()
                elif choice == 3:
                    query = input("Enter Name or Phone Number to Search: ").strip()
                    self.search_contact(query)
                elif choice == 4:
                    query = input("Enter Name or Phone Number to Update: ").strip()
                    self.update_contact(query)
                elif choice == 5:
                    query = input("Enter Name or Phone Number to Delete: ").strip()
                    self.delete_contact(query)
                elif choice == 6:
                    print("Exiting Contact Book. Goodbye!")
                    break
                else:
                    print("Invalid choice! Please select a valid option.")
            except ValueError:
                print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    app = ContactBook()
    app.run()

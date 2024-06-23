class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        return results

    def update_contact(self, query, name=None, phone=None, email=None, address=None):
        results = self.search_contact(query)
        if results:
            results[0].update(name, phone, email, address)
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, query):
        results = self.search_contact(query)
        if results:
            self.contacts.remove(results[0])
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        
        elif choice == '2':
            contact_book.view_contacts()
        
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(query)
            if results:
                for contact in results:
                    print(contact)
            else:
                print("No contacts found.")
        
        elif choice == '4':
            query = input("Enter name or phone number to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            contact_book.update_contact(query, name, phone, email, address)
        
        elif choice == '5':
            query = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(query)
        
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

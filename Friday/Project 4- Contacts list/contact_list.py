import os.path

class Contact:
    def __init__(self, contact_id, first_name, last_name, phone_number):
        self._contact_id = contact_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    @property
    def contact_id(self):
        return self._contact_id

    def display_data(self):
        print("ID: " + str(self.contact_id))
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Phone number: " + self.phone_number)

class ContactList:
    def __init__(self):
        self._filename = "contacts.txt"
        self.contacts = []
        self._current_id = 1
        
        if os.path.exists(self._filename):
            f = open(self._filename, "r")
            for line in f:
                ln = line.strip("\n")
                arr = ln.split(",")
                new_contact = Contact(int(arr[0]), arr[1], arr[2], arr[3])
                self.contacts.append(new_contact)
            f.close()
            self._current_id = self.contacts[-1].contact_id + 1

    @property
    def current_id(self):
        return self._current_id

    def add_contact(self, first_name, last_name, phone_number):
        new_contact = Contact(self.current_id, first_name, last_name, phone_number)
        self.contacts.append(new_contact)
        print("Contact added.\n")
        self._current_id += 1
        return new_contact

    def remove_contact(self, contact_id):
        self.contacts = [contact for contact in self.contacts if contact.contact_id != contact_id]
        print("Done.\n")

    def print_list(self):
        print("Contact list: \n")
        for contact in self.contacts:
            contact.display_data()
            print()
        print()

    def save_changes(self):
        f = open(self._filename, "w")
        for contact in self.contacts:
            f.write(str(contact.contact_id) + "," + 
                    str(contact.first_name) + "," +
                    str(contact.last_name) + "," +
                    str(contact.phone_number) + "\n")
        f.close()
        print("Changes saved!")


my_phonebook = ContactList()

while True:
    print("Enter 1 to view phonebook")
    print("Enter 2 to add a new contact")
    print("Enter 3 to delete a contact")
    print("Enter 4 to save all changes")
    print("Enter anything else to quit")
    response = input("Your input: ")

    if response == "1":
        my_phonebook.print_list()
    
    elif response == "2":
        first_name = input("First name: ")
        last_name = input("Last name: ")
        phone_number = input("Phone number: ")
        new_contact = my_phonebook.add_contact(first_name, last_name, phone_number)
        print("ID = " + str(new_contact.contact_id))
        print("First name = " + new_contact.first_name)
        print("Last name = " + new_contact.last_name)
        print("Phone number = " + new_contact.phone_number + "\n")
    
    elif response == "3":
        contact_id = int(input("Enter contact ID to delete: "))
        my_phonebook.remove_contact(contact_id)
    
    elif response == "4":
        my_phonebook.save_changes()
    
    else:
        print("\nGoodbye!")
        break
    

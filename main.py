#Funtions for necessary actions
def add_contacts(contacts):
    new_contact = {
        "name": input('Enter the name '),
        "number": input('Enter the phone number '),
        "email": input('Enter the email address ')
    }
    contacts.append(new_contact)


def show_contacts(contacts):
    for contact in contacts:
        print(contact['name'])


#delete files
def delete_contacts(contacts, name):
    name_lower = name.lower()
    for contact in contacts:
        if contact['name'].lower() == name_lower:
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
            save_contacts_to_file(contacts)  # Save changes to the file
            return
    print(f"Contact '{name}' not found.")




def update_contacts(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            contact["number"] = input('Enter the phone number ')
            contact["email"] = input('Enter the email ')
            print(f"Contact '{name}' updated successfully.")
            return
    print(f"Contact '{name}' not found.")


def open_contacts(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            print(f"name: {contact['name']}, phone: {contact['number']}, email: {contact['email']}")
            return
    print(f"Contact '{name}' not found.")

#File path implementations to store 
def save_contacts_to_file(contacts, filename='Contact_directory.txt'):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['number']}|{contact['email']}\n")

#This one is for retrieving
def load_contacts_from_file(filename='Contact_directory.txt'):
    contacts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, number, email = line.strip().split('|')
                contact = {"name": name, "number": number, "email": email}
                contacts.append(contact)
        return contacts
    except FileNotFoundError:
        return []


contacts = load_contacts_from_file()


#Takes input to carry out necessary actions

while True:
    show_contacts(contacts)
    action = input("press 'a' - add contact, 'o' -open contact, 'u' -update contact,'d' - delelte a contact, q' quit :> ")
    if action == 'a':
        add_contacts(contacts)
        save_contacts_to_file(contacts)
    elif action == 'o':
        name = input('Enter the name of your contact you want to open: ')
        open_contacts(contacts, name)
    elif action == 'u':
        name = input('Enter the name of your contact you want to update: ')
        update_contacts(contacts, name)
        save_contacts_to_file(contacts)
    elif action=='d':
        name=input('Enter the name ')
        delete_contacts(contacts, name)
    elif action == 'q':
        break
    else:
        print("Invalid output")

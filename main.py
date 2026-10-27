print("Welcome")
contacts = {}
def add_contact() :
    name = input("Enter name: ").lower().replace(" ", "")
    if not name.isalpha():
        print("Invalid name!")
        return
    phone = input("Enter phone number: ")
    if len(phone) != 11 or not phone.isdigit():
        print("Invalid number!")
    else :
        contacts[name] = phone
        print("Added successfully!")
    return
def list_contacts():
    if contacts == {} :
        print("No contacts found!")
    else :
        for names,phones in contacts.items():
            print(f"{names}: {phones}")
    print()
    return
def search_contact() :
    search = input("Search contact: ").lower().replace(" ","")
    if search in contacts :
        print(f"{search}: {contacts[search]}")
    else :
        print("Contact doesn't exist!")
    return
def delete_contact() :
    delete = input("Enter contact to delete: ").lower().replace(" ","")
    if delete in contacts :
        contacts.pop(delete)
        print("Deleted successfully")
    else :
        print("Contact doesn't exist!")
    return

while True :
    print("1. Add a contact(name and phone number)")
    print("2. List all contacts")
    print("3. Search for a contact by name")
    print("4. Delete a contact")
    print("5. Exit\n")
    try :
        option = int(input("Choose option: "))
    except ValueError:
        print("Choose a vailid option")
        continue
    if option == 1 :
        add_contact()
    elif option == 2 :
        list_contacts()
    elif option == 3 :
        search_contact()
    elif option == 4 :
        delete_contact()
    elif option == 5 :
        break
    
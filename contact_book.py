contact_list = {}

def show_contact():
    print('Name\t\tContact Number')
    for name in contact_list:
        print(f'{name}\t\t{contact_list.get(name)}')
while True:
    choice = int(input(" 1. Create contact \n 2. Add new contact \n 3. Update contact \n 4. Delete contact \n 5. Search contact \n 6. Show all contact \n -->"))

    if (choice == 1):
        name = input('Enter the contact name\n')
        number = input('Enter the mobile number\n')

        contact_list[name]=number

    if (choice == 2):
        contact_name = input('Enter the contact name\n')
        number2 = input('Enter the mobile number:\n')
        if contact_name in contact_list:
            try:
                if contact_list[contact_name].isnumeric():

                    number1 = contact_list.get(contact_name)
                    contact_list[contact_name]=[]
                
                    contact_list[contact_name].append(number1)
                    contact_list[contact_name].append(number2)
            except AttributeError:
                contact_list[contact_name].append(number2)
            finally:
                show_contact()
        else:
            print('Name not found in contact book')
            
    if (choice == 3):
        edit_contact = input('Enter the contact to be edited\n')
        if edit_contact in contact_list:
            number = input('Enter the mobile number\n')
            contact_list[edit_contact]=number
            print('Contact updated')
            print('Name\t\tContact Number')
            print(f'{edit_contact}\t\t{contact_list.get(edit_contact)}')
        else:
            print('Name not found in contact book')

    if (choice == 4):
        del_contact = input('Enter the contact to be deleted\n')
        if del_contact in contact_list:
            confirm = input('Are you sure to delete: y/n\n')
            if confirm == 'y' or confirm == 'Y':
                contact_list.pop(del_contact)
            show_contact()
        else:
            print('Name not found in contact book')

    if (choice == 5):
        search_name = input('Enter the contact name\n')

        if search_name in contact_list:
            print(search_name,' ', contact_list[search_name])
        else:
            print('Name not found in contact book')

    if (choice == 6):
        if not contact_list:
            print('Empty contact list')
        else:
            show_contact()

    close = input('Want to close the contact book: y/n \n -->')
    if close=='y' or close=='Y':
        break

print("*************** Programmed by ******************")
print("***** Carla Jeanne Golena & Noriel Cahilig *****")
print("****************** BSCOE 1-3 *******************\n\n")


# --------------LAST STOP ------------------#


def contact():
    for i in range(num):
        first_name = input("\nEnter first name: ")
        last_name = input("Enter last name: ")
        address = input("Enter address: ")
        phone_num = int(input("Enter phone number: "))
        first_names.append(first_name)
        last_names.append(last_name)
        names.append(first_name + " " + last_name)
        homes.append(address)
        phone_numbers.append(phone_num)


def menu():
    print("-------------- Address Book ------------------\n")
    print("What would you like to do? \n")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Search Address Book")
    print("6. Exit\n")


names = []
first_names = []
last_names = []
homes = []
phone_numbers = []
num = 1
choice2 = 'y'
choice = 0
entry = list(range(1, 100))

while choice2 == 'y' and choice != 6:
    menu()
    choice = int(input("Choose an option: "))
    if choice == 1:  # -ADD CONTACT-
        contact()
        print("\nNew contact added.")

    elif choice == 2:  # -EDIT CONTACTS-
        print(
            """
            What do you want to edit:
            1. Full Name
            2. Contact Number
            3. Address
            """
        )
        edit = int(input("What would like to edit(1/2/3)? "))
        if edit == 1:
            a = input("Enter full name: ")
            if a in names:
                b = input("Enter new full name: ")
                for i in range(len(names)):
                    if names[i] == a:
                        names[i] = b
                print("Contact Updated.")
            else:
                print("\nName not recognized. ")
        elif edit == 2:
            a = int(input("What phone number you want to edit: "))
            if a in phone_numbers:
                b = int(input("Enter new phone number: "))
                for i in range(len(phone_numbers)):
                    if phone_numbers[i] == a:
                        phone_numbers[i] = b
                print("Contact Updated.")
            else:
                print("\nNumber not recognized. ")
        elif edit == 3:
            a = input("What address you want to edit: ")
            if a in homes:
                b = input("Enter new address: ")
                for i in range(len(homes)):
                    if homes[i] == a:
                        homes[i] = b
                print("\nContact Updated.")
            else:
                print("Address not recognized. ")

    elif choice == 3:  # -DELETE-
        delete = input("Enter contact you want to delete:")

        if delete in names:
            del_index = names.index(delete)
            names.remove(delete)
            del phone_numbers[del_index]
            del homes[del_index]
            print("Contact Deleted.")
        else:
            print("\nNumber is not recognized.")

    elif choice == 4:  # -VIEW-
        print("\t\t", "NAME", "\t\t", "ADDRESS", "\t\t", "PHONE NUMBER")
        for x in range(len(names)):
            print(entry[x], "\t", names[x], "\t", homes[x], "\t", phone_numbers[x])

    elif choice == 5:  # -SEARCH CONTACT-
        print(
            """
            Search Using:
            a. Full Name
            b. Contact Number
            """
        )
        search = input("How would you like to search(a/b)? ")
        if search == "a":
            a = input("Enter full name: ")
            a_index = names.index(a)
            if a in names:
                print("NAME", "\t\t\t", "ADDRESS", "\t\t", "PHONE NUMBER")
                print(names[a_index], "\t", homes[a_index], "\t", phone_numbers[a_index])
            else:
                print("Name is not recognized")
        elif search == "b":
            b = input("Enter contact number: ")
            b_index = phone_numbers.index(b)
            if b in phone_numbers:
                print("NAME", "\t\t\t", "ADDRESS", "\t\t", "PHONE NUMBER")
                print(names[b_index], "\t", homes[b_index], "\t", phone_numbers[b_index])
            else:
                print("Number is not recognized")

    elif choice == 6:  # -EXIT-
        print("Thanks for using the program.")
        exit()


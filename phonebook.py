phonebook = {}


def format_name(name):
    """Formats name to standard"""
    name = name.casefold().title()
    return name


def in_phonebook(name):
    """Checks if name is already in phonebook"""
    if len(phonebook) > 0:
        for i in phonebook.keys():
            if name.casefold() == i.casefold():
                return True
            else:
                return False
    else:
        return False


def show_phonebook():
    """Print all contacts in the phonebook."""
    for (name, phonenumber) in phonebook.items():
        print(name, ':', phonenumber)


def add_contact():
    """Add contact to the dictionary"""
    name = input("Type a name: ")

    if in_phonebook(name):
        print("This name is already in the register.")
    else:
        phonenum = input("Type a phone number: ")
        name = format_name(name)
        phonebook[name] = phonenum


def remove_contact():
    """Remove contact from the dictionary"""
    name = input("Type a name: ")
    if in_phonebook(name):
        name = format_name(name)
        del phonebook[name]
        print(name + " has been deleted from the register.")
    else:
        print("This name is not in the register.")


def find_contact():
    """Finds contact in dictionary by name"""
    name = input("Type a name: ")

    if in_phonebook(name):
        name = format_name(name)
        print(name, ':', phonebook[name])
    else:
        print("This name is not in the register.")


def menu():
    """Display a menu, and ask the user to choose an option.
    Ensures that the chosen option is valid."""
    while True:
        print()
        print("0: Quit")
        print("1: Print all contacts")
        print("2: Add contact")
        print("3: Remove contact")
        print("4: Look up contact by name")
        print()

        inp = input("> ")
        if inp.isdigit():
            i = int(inp)
            if 0 <= i <= 4:
                return i

        print("INVALID INPUT")


def main():
    """Main loop, where the menu is shown, the user chooses an option,
    and the relevant code is run."""
    while True:
        i = menu()

        if i == 0:
            break
        elif i == 1:
            show_phonebook()
        elif i == 2:
            add_contact()
        elif i == 3:
            remove_contact()
        elif i == 4:
            find_contact()


if __name__ == "__main__":
    main()
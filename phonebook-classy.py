phonebook = []


class Contact:

    def __init__(self, name, phonenum, email="", address="", birthday="", job=""):
        self._contact = {
            "name": name,
            "phonenumber": phonenum,
            "email": email,
            "address": address,
            "birthday": birthday,
            "job": job
        }
        self._name = name

    def show(self):
        for i in self._contact.keys():
            item = self._contact.get(i)
            if item != "":
                print(i.title() + " : " + item)


my_contact = Contact("Klaus Marianne", "23578932", "klaus.m@gmail.com", birthday="03.03.2003", job="Nurse")

my_contact.show()


def format_name(name):
    """Formats name to standard"""
    name = name.casefold().title()
    return name


def in_phonebook(name):
    """Checks if name is already in phonebook"""
    if len(phonebook) > 0:
        for i in phonebook:
            if name.casefold() == i._name.casefold():
                return phonebook.index(i)
                print("Other" + phonebook.index(i))
            else:
                return False
                print("Name not right " + phonebook.index(i))
    else:
        return False
        print("mistake is length")



def show_phonebook():
    """Print all contacts in the phonebook."""
    for i in phonebook:
        i.show()


def add_contact():
    """Add contact to the dictionary"""
    name = input("Type a name: ")

    if in_phonebook(name):
        print("This name is already in the register.")
    else:
        phonenum = input("Type a phone number: ")
        email = input("Type an email or SPACE to skip: ")
        address = input("Type an address or SPACE to skip: ")
        birthday = input("Type a date or SPACE to skip: ")
        job = input("Type an occupation or SPACE to skip: ")
        name = format_name(name)

        phonebook.append(Contact(name, phonenum, email, address, birthday, job))


def remove_contact():
    """Remove contact from the dictionary"""
    name = input("Type a name: ")
    if not in_phonebook(name):
        print("This name is not in the register.")
    else:
        del phonebook[in_phonebook(name)]
        print(name + " has been deleted from the register.")


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
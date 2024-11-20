from Commands import parse_input, add_contact, change_contact, show_all, show_phone, add_birthday, show_birthday, birthdays
from Phone_book import AddressBook


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command is None:
            print("Please enter a command.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        elif command == "help":
            print("exit", "hello", "add", "change", "phone", "all", "add-birthday" ,"show-birthday", "birthdays", sep="\n")

        else:
            print("Invalid command, type 'help' to see all commands")


if __name__ == "__main__":
    main()
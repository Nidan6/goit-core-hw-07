from collections import UserDict
from datetime import datetime, timedelta, date

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

        self.value = value

        if not value.isdigit() or len(value) != 10:
            raise ValueError

class Birthday (Field):
    def __init__(self, value):
        super().__init__(value)
        try:
            datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for index, del_phone in enumerate(self.phones):
            if del_phone.value == phone:
                return self.phones.pop(index)


    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[index] = Phone(new_phone)
                return new_phone
            raise ValueError

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)


    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = f", Birthday: {self.birthday.value}" if self.birthday else ""
        return f"Name: {self.name.value}, Phones: {phones}{birthday}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        if record.name.value in self.data:
            return None
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def get_upcoming_birthday(self, days=7):
        upcoming = []
        today = date.today()
        for record in self.data.values():
            if record.birthday:
                birthday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday.replace(year=today.year)

                if 0 <= (birthday_this_year - today).days <= days:
                    upcoming.append({
                        "name": record.name.value,
                        "birthday": birthday_this_year.strftime("%d.%m.%Y")
                    })
            return upcoming

    

    def __str__(self):
        return "\n".join(f"{name}: {record}" for name, record in self.data.items())

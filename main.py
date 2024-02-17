from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.name} {self.surname} {self.phone_number} {self.email}"
    
    def __repr__(self):
        return f"BaseContact(name={self.name}, surname={self.surname}, phone number={self.phone_number}, email={self.email})"

    def contact(self):
        print()
        print("-----------Wizytówka normalna-----------")
        print(f"Wybieram numer {self.phone_number} i dzwonie do {self.name} {self.surname}")
        print("------------------------------")

    @property
    def label_length(self):
        return len(self.name) + len(self.surname)


class BusinessContact(BaseContact):
    def __init__(self, position, company_name, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.company_phone = company_phone

    def contact(self):
        print()
        print("-----------Wizytówka biznesowa-----------")
        print(f"Wybieram numer {self.company_phone} i dzwonie do {self.name} {self.surname}")
        print("------------------------------")


def create_contacts(card_type, amount):
    print("Program generuje losowo generowane wizytówki\n")
    
    contact_list = []

    for i in range(int(amount)):
        full_name = fake.name()
        first_name, last_name = full_name.split(" ", 1)

        if card_type == '1':
            contact = BusinessContact(name=first_name, surname=last_name, phone_number=fake.phone_number(), email=fake.email(), position='boss', company_name=full_name, company_phone=fake.phone_number())
        elif card_type == '2':
            contact = BaseContact(name=first_name, surname=last_name, phone_number=fake.phone_number(), email=fake.email())
        contact_list.append(contact)

    return contact_list

def main():
    card_type = input("Wpisz rodzaj wizytowki: 1- Biznesowa, 2- Normalna: ")
    amount = input("Wpisz ilosc wizytowek jaka chcesz wygenerowac: ")
    contacts = create_contacts(card_type, amount)
    
    for contact in contacts:
        contact.contact()

if __name__ == '__main__':
    main()
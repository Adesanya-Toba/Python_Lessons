class Contact:
    all_contacts = []

    def __init__(self, name='', email='', **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street='', city='', state='', code='',
                 **kwargs) -> None:
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)

def main():
    Friend(phone='901', name= 'Toba', email= 'toba@you.com')


if __name__ == '__main__':
    main()

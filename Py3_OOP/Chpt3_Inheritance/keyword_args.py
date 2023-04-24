class Contact:
    all_contacts = []

    def __init__(self, name='', email='', **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        # self.phone = phone
        self.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street='', city='', state='', code='', phone='',
                 **kwargs) -> None:
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, **kwargs):
        # if we want 'phone' to be available in the kwargs dictionary,
        # we could update kwargs before calling super.
        # kwargs.update(dict(phonez=phone))
        # OR
        # kwargs.update({'phone': phone})
        # print(kwargs)
        super().__init__(**kwargs)
        self.phone = kwargs['phone']
        print(self.phone)

    def assign(self,age, **kwargs):
        self.age = age
        self.my_name = kwargs['name']
        self.payload = kwargs['payload']
        print(self.payload)

def main():
    AFriend = Friend(name='Toba', email= 'Toba@you.com', phone= 901)
    print(AFriend)

    AFriend.assign(27, name= AFriend.name, payload= 'Hello, how are you')


if __name__ == '__main__':
    main()

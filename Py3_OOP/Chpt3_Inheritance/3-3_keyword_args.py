class Contact:
    all_contacts = []

    def __init__(self, name='', email='', **kwargs) -> None:
        print(kwargs)
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        # self.phone = phone
        self.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street='', city='', state='', code='',
                 **kwargs) -> None:
        print(kwargs)
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, **kwargs):
        # if we want 'phone' to be available in the kwargs dictionary,
        # we could update kwargs before calling super.
        # kwargs.update(dict(phone=phone))
        # OR
        # kwargs.update({'phone': phone})
        # print(kwargs)
        # OR
        # We could remove phone as an explicit argument and let kwargs handle
        # Friend can get the value of phone by looking it up in the kwargs dictionary
        '''NOTE: When using **kwargs in super().__init__(), ensure the init functions 
        of at least one of the parent classes require all or some the items in kwargs,
        as kwargs will be unpacked (i.e. elements will be exported to the parameter list
        of the init function and deleted from kwargs) and must be empty by the time the 
        call to super() is reached.
        This is only necessary if the init function of parent class also calls 
        super().__init(**kwargs).'''
        print(kwargs)
        new_kwargs = collect_kwargs(**kwargs)
        print(new_kwargs)
        super().__init__(new_kwargs)
        self.phone = kwargs['phone']
        print(self.phone)

    def assign(self,age,name, **kwargs):
        self.age = age
        # self.my_name = kwargs['name']
        self.payload = kwargs['payload']
        print(self.payload)
        print(kwargs)

def collect_kwargs(name, phone, **kwargs):
    return kwargs

def main():
    AFriend = Friend(name='Toba', email= 'Toba@you.com', phone= 901)
    print(AFriend)

    AFriend.assign(27, name= AFriend.name, payload= 'Hello, how are you', more_data='hello again')


if __name__ == '__main__':
    main()

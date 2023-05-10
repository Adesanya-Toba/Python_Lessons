'''All python classes automatically inherit from the base class: object'''
class MySubClass(object):
    pass

# Inheriting/Extending built-ins
class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value in their name'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

# Extending the dictionary class
class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest
    

class Contact:
    all_contacts = [] # this is shared by all instances/objects of this class using Contact.all_contacts
    searchable_contacts = ContactList()

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.searchable_contacts.append(self) # Adding this object to its own version of searchable_contacts
        Contact.all_contacts.append(self) # Adding this object to the all_contacts variable

    # Adding a representation method for the object
    def __repr__(self) -> str:
        '''Creates a representation of an object, so that our objects
        look more meaningful when called with print(object).
        '''
        return (
            f'{self.__class__.__name__}('
            f'{self.name!r}, {self.email!r}'
            f')'
        )


class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send"
                " '{}' order to '{}'".format(order, self.name))
    

def main():
    print(f'{Contact.all_contacts}\n') 
    AContact = Contact('Toba', 'toba@gmail.com')
    BContact = Contact('Ebun1', 'ebun@gmail.com')
    CContact = Contact('Ebun2', 'ebun@gmail.com')

    TSupplier = Supplier('Shawn', 'shawn@gmai.com')

    TSupplier.order('maggi')

    print(f'{Contact.all_contacts}\n') 
    for v in Contact.all_contacts:
        print(f'{v.name}, {v.email}')
    
    print()

    for v in Contact.searchable_contacts:
        print(f'{v.name}, {v.email}')
        

    # Using search functionality in ContactList
    r = [c.name for c in Contact.searchable_contacts.search('Ebun')]

    # Same as the above
    d = []
    for c in Contact.searchable_contacts.search('Ebun'):
        d.append(c.name)
    
    print(f'd list: {d}')
    print(f'r list: {r}')

    # Creating an instance of and testing the LongNameDict class
    longkeys = LongNameDict()

    longkeys['hello'] = 1
    longkeys['longest yet'] = 20
    longkeys['hello2'] = 'halleluyah'

    print(longkeys.longest_key())

    print()
    print(AContact)

if __name__ == '__main__':
    main()
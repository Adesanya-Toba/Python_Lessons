'''All python classes automatically inherit from the base class: object'''
class MySubClass(object):
    pass

class Contact:
    all_contacts = [] # this is shared by all instances/objects of this class using Contact.all_contacts

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self) # Adding this object to the all_contacts variable


class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send"
                " '{}' order to '{}'".format(order, self.name))


def main():
    print(f'{Contact.all_contacts}\n') 
    AContact = Contact('Toba', 'toba@gmail.com')
    BContact = Contact('Ebun', 'ebun@gmail.com')

    TSupplier = Supplier('Shawn', 'shawn@gmai.com')

    TSupplier.order('maggi')

    print(f'{Contact.all_contacts}\n') 
    for v in Contact.all_contacts:
        print(f'{v.name}, {v.email}')

if __name__ == '__main__':
    main()
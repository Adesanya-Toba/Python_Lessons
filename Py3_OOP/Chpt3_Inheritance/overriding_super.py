class Contact:
    all_contacts = []

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self) # Adding this object to the all_contacts variable

    def this_function():
        pass

class Friend(Contact):
    def __init__(self, name, email, phone) -> None:
        # Super gets an instance of the parent class and then calls the function 
        # This can be __init__ or any other function in the parent class
        super().__init__(name, email)
        self.phone = phone

# Multiple Inheritance 
'''Rule of Thumb
If you think you need multiple inheritance, you're wrong and you don't.
If you know you need multiple inheritance, then you're right and you do.
'''

# A Mixin is simple form of multiple inheritance
'''It's a superclass that is not meant to exist on its own but is meant to 
inherited by some other class to provide extra functionality.
'''

# Adding an email sender mixin
class MailSender:
    def send_mail(self, message):
        print('Sending mail to ' + self.email)

# Now we can inherit from it and the contact class like so
class EmailableContact(Contact, MailSender): # Inheriting from multiple classes
    pass


def main():
    AContact = EmailableContact('Bruce', 'bruce@rocketmail.com')

    AContact.send_mail('Does this even work?')

    print(Contact.all_contacts)

if __name__ == '__main__':
    main()
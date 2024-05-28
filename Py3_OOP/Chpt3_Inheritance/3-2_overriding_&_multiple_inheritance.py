class Contact:
    all_contacts = []

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(
            self
        )  # Adding this object to the all_contacts variable

    def this_function():
        pass


class Friend(Contact):
    def __init__(self, name, email, phone) -> None:
        # Super gets an instance of the parent class and then calls the function
        # This can be __init__ or any other function in the parent class
        super().__init__(name, email)
        self.phone = phone

        # We could also call super this way. Using the parent class explicitly
        Contact.__init__(self, name, email)  # Not recommended, super's the way to go.


# Multiple Inheritance
"""Rule of Thumb
If you think you need multiple inheritance, you're wrong and you don't.
If you know you need multiple inheritance, then you're right and you do.
The problem arises when you need to make calls to the super class but since 
you have multiple superclasses, how do you know which one you're calling or the 
order in which to call them.
"""

# A 'Mixin' is simple form of multiple inheritance
"""It's a superclass that is not meant to exist on its own but is meant to be
inherited by some other class to provide extra functionality.
"""


# Adding an email sender mixin
class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)


# Now we can inherit from it and the contact class like so
class EmailableContact(Contact, MailSender):  # Inheriting from multiple classes
    pass


class AddressHolder:
    def __init__(self, street, city, state, code) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.code = code


# The diamond problem of Multiple inheritance where a base class gets called more than one
# can be solved using super(). For example,
class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1


class LeftSubClass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print("Calling method on Left subclass")
        self.num_left_calls += 1


class RightSubClass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print("Calling method on Right subclass")
        self.num_right_calls += 1


class Subclass(LeftSubClass, RightSubClass):
    num_sub_calls = 0

    def call_me(self):
        """Calling the left and right subclasses explicitly would have cause the
        base class to be called twice
        However using super avoids this by ensuring the base class is only called
        once. This works by calling the next method in the inheritance hierarchy
        not necessarily the parent method.
        It works but I don't think I like it.
        """
        LeftSubClass.call_me(self)
        # RightSubClass.call_me(self)
        # super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1


def main():
    # a_contact = EmailableContact("Bruce", "bruce@rocketmail.com")
    # b_friend = Friend("Miles", "miles@outlook.com", 123456779)

    # a_contact.send_mail("Does this even work?")

    # print(Contact.all_contacts)

    # Testing multiple inheritance
    s = Subclass()
    s.call_me()

    # print(s.num_sub_calls, s.num_left_calls, s.num_right_calls, s.num_base_calls)


if __name__ == "__main__":
    main()

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

# Using positional arguments
print("Start")
greet_user("John", "Smith")
print()
greet_user("Mary", "Kay")
print("Finish")
print()


# Using Keyword arguments
greet_user(last_name="John", first_name="Smith")
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print('Enjoy your day')
print()

price = 1000000
good_credit = False
if good_credit:
    payment = 0.1 * price
else:
    payment = 0.2 * price

print(f"Put down ${int(payment)}! ")
print()


# Logical operators
# and, or, not
has_high_income = True
has_good_credit = True

if has_high_income and not has_good_credit:
    print('Eligible for loan')


# Comparison operators
# equal ==, not equal !=, greater >, lesser <, greater or equal >=, lesser or equal <=

temperature = 35
if temperature >= 30:
    print("It's a hot day")
else:
    print("it's a cold day")

name = input('Enter your name please: ')
if len(name) < 3:
    print("!! Name must be at least 3 characters")
elif len(name) > 50:
    print("!! Name can be a maximum of 50 characters")
else:
    print("Looks good!")

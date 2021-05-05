print("Adesanya Toba")

Amari = True
is_asleep = False

name = input('What is your name? ')
color = input('Okay, what is  your favourite color? ')
birth_year = input('When where you born? ')  # input always stores values as strings

print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age))

print()
print(name + ' likes ' + color + ' color!')
print('He is ' + str(age) + ' years')

# another example. Converting from pounds to kilograms
weight_lbs = input("How much do you weigh(in pounds): ")
weight_kg = float(weight_lbs) * 0.4536
print('Your weight in kilogram is: ' + str(weight_kg) + 'kg')

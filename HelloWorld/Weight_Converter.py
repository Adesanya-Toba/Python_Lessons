weight = float(input("Enter your weight: "))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'KG':
    weight_lbs = weight / 0.45
    # weight_lbs = float("{:.2f}".format(weight_lbs))
    weight_lbs = round(weight_lbs, 2)
    print(f"You are {weight_lbs} pounds")
elif unit.upper() == 'LBS':
    weight_kg = round((weight * 0.45) , 2)
    print(f"You are {weight_kg} kilograms")

a = 13.4873749993773764767209827
print(round(a, 2))  # round(arg, number), limits the number of decimal places
print("{:.2f}".format(a))  # "{:.2f}".format, limits to 2 decimal places
# Except "{:.2f}" returns a string, so you have to recast to int or float
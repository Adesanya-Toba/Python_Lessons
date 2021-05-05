try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(risk)
except ZeroDivisionError:
    print("Age cannot be zero!")
except ValueError:
    print("Invalid value!")

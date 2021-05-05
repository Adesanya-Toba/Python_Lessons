names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[2:4])  # creates a new list of names
names[0] = "Jon"  # List strings are saved in single quotes
print(names)
print()

# Adding all elements in a list
numbers = [5, 13, 3, 8, 10, 99, 11]
total = 0
for i in numbers:
    total += i

print(str(total) + '\n')

# Finding the greatest number
greatest = numbers[0]
for x in numbers:
    if x > greatest:
        greatest = x

print(f"The greatest number is: {greatest}")


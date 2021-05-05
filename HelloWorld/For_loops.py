for item in "Python":
    print(item)  # Prints all the elements in the Python string
print()

for number in [1, 2, 3, 4, 5]:
    print(number)
print()

prices = [10, 20, 30]  # this is called a List
total = 0
for item in prices:
    total += item

print(f"Total is: {total}\n")

# Range function returns a range object. range(starting number, stopping number -1, step)
for number in range(2, 11, 2):  # range of numbers: from 2 to 10, in steps of 2 i.e. even numbers
    print(number)

for n in range(1000):  # Busy wait from 0 to 999
    print(n)

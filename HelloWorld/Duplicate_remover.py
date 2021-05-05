# A PROGRAM THAT REMOVES THE DUPLICATES FROM A LIST
program = [1, 9, 9, 2, 8, 1, 8, 2, 2, 8, 8, 9, 1, 9]

program.sort()  # Better to sort first, this piece of code is weird
for item in program:
    while (program.count(item)) != 1:
        # print(program)
        # print(f"{item}: {program.count(item)}")
        program.remove(item)

print(program)

# ANOTHER METHOD
numbers = [1, 9, 9, 2, 8, 1, 8, 2, 2, 8, 8, 9, 1, 9]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
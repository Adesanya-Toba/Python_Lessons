for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
print()

numbers = [5, 2, 4, 2, 2]
for x2 in numbers:
    shape = ""
    for y in range(x2):
        shape += 'x'
    print(shape)
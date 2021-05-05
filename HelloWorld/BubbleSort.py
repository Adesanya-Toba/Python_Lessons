# Finding the greatest number
no = 1
# 5, 13, 3, 8, 10, 9, 11, 78, -1, 0
numbers = [5, 13, 3, 8, 10, 9, 11, 78, -1, 0]
# Arrange the list first
for x in range(len(numbers)):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]  # Perform a swap
            numbers[i+1] = temp
            print(f"{no}: {numbers}")
            no += 1

# Then print the number at the 'last index' which would now be the greatest
print(f"The greatest number is: {numbers[-1]}")


for x in range(7):
    print(x)
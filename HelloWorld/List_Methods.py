numbers = [5, 2, 1, 7, 5, 4]
print(f"original: {numbers}")

numbers.append(20)  # Appends to the end of the list
print(f"append, 20: {numbers}")

numbers.insert(0, 10)  # Insert at any index you want. First arg is index, second is object
print(f"insert, 10 at 0th: {numbers}")

numbers.remove(10)  # Remove number if it exists
print(f"remove, 10: {numbers}")

numbers.reverse()  # Reverses the whole list. Soo easy!
print(f"reverse: {numbers}")

print(f"index of 20: {numbers.index(20)}")  # Checks if the number exists in the list and prints the index

print(50 in numbers)  # Prints out either true or false. Safer to use than 'index'

print(numbers.count(5))  # Prints the number of occurrences in the list

# To sort a list. Too easy, almost unfair!
numbers.sort()
print(f"sorted list: {numbers}")

numbers2 = numbers.copy()
print(f"Copied list: {numbers2}")


numbers.pop()  # Pops the last element in the list
print(f"pop: {numbers}")

numbers.clear()  # Clears the whole list
print(f"clear: {numbers}")

print(f"Copied list: {numbers2}")



course = "Python's for beginners"
course2 = '''
Hi John's mum,

This is our first email to you.

We wanted to find out how you are doing? Since John mentioned
"you were sick!"

Thank you.
The Support team.
'''
print(course[0])  # index of first character
print(course[-1])  # index of last character

print(course[0:3])  # print from first index to 2nd index
print(course[2:3])  # same as writing course[2]

print(course[0:])  # prints all characters from the 0th index
print(course[1:])  # prints all characters from the 1th index

print(course[:6])  # prints all characters till the 5th index. Sorry feeling lazy

another = course[:]  # copies string. Assumes 0 as the start and the last character as the end.
print(another)
print()
name = 'Jennifer'
print(name[1:-1])
print()


# Formatted Strings
# We want to print 'John [Smith] is a coder.'
first = 'John'
last = 'Smith'
message = f'{first} [{last}] is a coder.'   # f'', defines a formatted string
print(message)
print()


# String Methods
title = 'Python for Beginners.'
print(len(title))  # len is a general purpose function. Returns length of elements

# .upper does not modify the variable but actually creates a new one and copy there
print(title.upper())  # upper is a String method cos it is specific to strings
print(title)

print(title.lower())  # lower case

print(title.find('for'))  # find: returns the starting index of the character or word
print(title.replace('Beginners', 'Absolute Beginners'))  # replace

print('yt' in title)  # 'in' operator returns a boolean value, unlike find

print(title.title())  # title captilalizes each word. 
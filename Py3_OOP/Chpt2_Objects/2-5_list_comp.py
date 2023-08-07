'''
List comprehension and Generator Expressions
'''

x = 'ABC'
# ord: returns the unicode point for each character
codes = [ord(char) for char in x]
# char is local and doesn't exist past the line above
print(codes)

# However, with the Walrus operator (:=), we could create variables that remain
# accessible after the comprehension returns

b_codes = [last:= ord(char) for char in x]
print('last: ', last)
print(b_codes)
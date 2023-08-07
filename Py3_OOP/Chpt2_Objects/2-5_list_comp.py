'''
List comprehension and Generator Expressions
A quick way to build a sequence is using a list comprehension (if the target is a list)
or a generator expression (for other kinds of sequences).
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

# Filtering using list comps
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

# Doing this without list comps would require the use of lambdas
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

import string

def format_string(string: string, formatter=None) -> string:
    '''Format a string using the formatter object, which
    is expected to have a format() method that accepts
    a string'''
    class DefaultFormatter:
        '''Format a string in Title case.'''
        def format(self, string):
            return str(string).title()
        
    if not formatter: # i.e. if a formatter object is not supplied
        formatter = DefaultFormatter()

    return formatter.format(string)

def main():
    hello_string = "hello world, how are you?"
    print(" input: " + hello_string)
    print(" output: " + format_string(hello_string))

if __name__ == "__main__":
    main()

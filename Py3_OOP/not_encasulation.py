import traceback as t

class SecretString:
    '''A not-at-all secret way to store a secret string'''

    def __init__(self, plain_string, pass_phrase):
        # Variables with double underscore preceeding them, get mangled by the interpreter.
        # this means, the interpreter preceeds the variable/attribute name with <_classname>
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

        # This is an internal attribute but it isn't mangled by the interpreter
        self._my_string = "yoo"

    def decrypt(self, pass_phrase):
        '''Only show string if the pass phrase is correct'''
        if (pass_phrase == self.__pass_phrase):
            return self.__plain_string
        return ' '
    
def main():
    my_secret = SecretString("Hello Toba", "ujmc")

    print(my_secret.decrypt("ujmc"))

    try:
        print(my_secret._my_string) # This would work fine
        print(my_secret.__plain_string) # This would result in a no attribute error

        # The new variable name afer interpreter mangles: _SecretString__plain_string
        print(my_secret._SecretString__plain_string)
    except Exception as e:
        print(f"You've just encountered an error on: {e}")
        print(t.format_exc())

    
if __name__ == "__main__":
    main()
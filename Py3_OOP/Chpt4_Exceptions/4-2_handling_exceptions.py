from typing import NoReturn, Union

def funny_division(divisor: float) -> Union[str,float]:
    try:
        return 100/divisor
    except ZeroDivisionError:
        return 'Zero is not a good idea'

def funnier_division(divisor: int) -> Union[str,float]:
    try:
        if divisor == 13:
            raise ValueError('13 is an unlucky number')
        return 100/divisor
    except (ZeroDivisionError, TypeError):
        return 'Enter a number other than zero'

def funniest_division(divisor:int) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError('13 is an unlucky number!')
        return 100/divisor
    except ZeroDivisionError:
        return 'Enter a number other than zero'
    except TypeError:
        return 'Enter a numerical value'
    except ValueError:
        print('No, No, not 13!')
        raise

def never_returns() -> NoReturn:
    print("I am about to raise an exception")
    raise ValueError("This is always raised")
    print("This line will never execute")
    return "I won't be returned"

def main() -> None:
    try:
        never_returns()
        print('Never executed!')
    except Exception as ex:
        print(f'I caught an exception: {ex!r}') # the !r simply prints the Exception line that was raise
    print('Executed after the exception')

    print(funniest_division(13))

if __name__ == '__main__':
    main()
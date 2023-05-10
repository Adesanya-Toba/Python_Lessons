# Interpolation operation in python
string = 'hello = %.2f' % 10.98
string2 = f'hello = {89.98}'
print(string)
print(string2)

def odd(n:int) -> bool:
    return n % 2 != 0

def main() -> None:
    odd(42)

if __name__ == '__main__':
    main()
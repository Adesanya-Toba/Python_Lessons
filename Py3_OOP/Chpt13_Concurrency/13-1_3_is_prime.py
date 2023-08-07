import math
import itertools
import time
from threading import Thread, Event

def spin(msg:str, done:Event):
    for char in itertools.cycle(r'\|/-'):
        status:str = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(0.1):
            break
    
    # print('Out of the for loop.')
    blanks = ' ' * len(status) # type:ignore
    print(f'\r{blanks}\r', end='')

def is_prime(n:int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True

def slow(n:int):
    # ans = is_prime(n)
    time.sleep(5)
    return 44

def supervisor() -> int:
    done = Event() # We use the Event instance to coordinate activities of the main and spinner thread

    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'Spinner object: {spinner}')
    spinner.start()

    # This calls slow and blocks the main thread while the secondary thread is running the spinner function
    result  = slow(5_000_111_000_222_021)

    # When the main thread sets the done event, the spinner thread will eventually notice
    # and exit cleanly
    done.set() # This sets the event flag to true and terminates the for loop inside the spin function

    spinner.join() # Wait until the spinner thread finishes
    return result

def main() ->None:
    result = supervisor() # This will return the result of slow
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()

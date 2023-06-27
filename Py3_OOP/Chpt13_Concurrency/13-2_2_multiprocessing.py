import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize

def spin(msg:str, done:synchronize.Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status:str = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(0.1):
            
            break

    blanks = ' ' * len(status) # type:ignore
    print(f'\r{blanks}\r', end='')

def slow():
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()

    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor() # This will return the result of slow
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()

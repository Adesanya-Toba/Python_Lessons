import itertools
import time
import logging
from multiprocessing import Process, Event
from multiprocessing import synchronize

logging.basicConfig(level=logging.DEBUG, format='%(processName)-11s %(threadName)-11s [%(levelname)s]: %(message)s')
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

# Notice multiprocessing.Event is a function (not a class like threading.Event)
# which returns a synchronize.Event instance

def spin(msg:str, done:synchronize.Event) -> None:
    logger.info('Inside spinner process.')
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
    done = Event() # Essentially a function call
    spinner = Process(target=spin, args=('thinking!', done))
    logger.info(f'spinner object: {spinner}')
    spinner.start()
    result = slow()

    done.set()
    spinner.join() # Wait for spinner process to finish
    return result

def main() -> None:
    result = supervisor() # This will return the result of slow
    logger.info(f'Answer: {result}')

if __name__ == '__main__':
    main()

import itertools
import time
from threading import Thread, Event

# The threading.Event class is Python’s simplest signalling mechanism to coordinate
# threads. An Event instance has an internal boolean flag that starts as False. Calling
# Event.set() sets the flag to True. While the flag is false, if a thread calls
# Event.wait(), it is blocked until another thread calls Event.set(), at which time
# Event.wait() returns True. If a timeout in seconds is given to Event.wait(s), this
# call returns False when the timeout elapses, or returns True as soon as Event.set()
# is called by another thread


def spin(msg:str, done:Event):
    for char in itertools.cycle(r'\|/-'):
        status:str = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(0.1):
            break
    
    # print('Out of the for loop.')
    blanks = ' ' * len(status) # type:ignore
    time.sleep(2)
    print(f'\r{blanks}\r', end='')


def slow():
    time.sleep(3)
    return 42


# The threading.Event instance is the key to coordinate the activities of the main
# thread and the spinner thread
def supervisor() -> int:
    done = Event() # We use the Event instance to coordinate activities of the main and spinner thread

    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'Spinner object: {spinner}')
    spinner.start()

    # This calls slow and blocks the main thread while the secondary thread is running the spinner function
    result  = slow()

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

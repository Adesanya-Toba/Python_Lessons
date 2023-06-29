import itertools
import asyncio
import time

#NOTE: invoking a coroutine as coro() immediately returns a
# coroutine object, but does not run the body of the coro function.
# Driving the body of coroutines is the job of the event loop.

def main() ->None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')

async def spin(msg:str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status:str = f'\r{char} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break

    blanks = ' ' * len(status) # type:ignore
    print(f'\r{blanks}\r', end='')

async def slow():
    print('in slow()')
    await asyncio.sleep(3.0)
    return 42

async def supervisor() -> int:
    # asyncio.create_task schedules the eventual execution of spin. It doesn't run immediately
    # but returns an instance of asyncio.Task
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinner object: {spinner}')
    

    # Called from a coroutine to transfer control to the coroutine object returned by coroutine().
    # i.e. called from supervisor to transfer control to the object returned by slow()
    # This suspends the current coroutine until the body of coroutine() i.e. slow() returns
    result = await slow()

    # This raises a CancelledError exception inside the spin coroutine and we use it to exit the for loop in spin
    spinner.cancel()
    return result

if __name__ == '__main__':
    main()
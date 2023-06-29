import itertools
import asyncio
import math

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

async def is_prime(n:int) -> bool:
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
        if i % 100_000 == 1:
            await asyncio.sleep(0) #call asyncio.sleep(0) in an await expression to yield control back to the event loop
    return True

async def slow():
    print('in slow()')
    ans = await is_prime(5_000_111_000_222_021)
    # await asyncio.sleep(3)
    return ans

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
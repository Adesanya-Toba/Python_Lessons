import asyncio
import random


# New since python 3.8: use 'async def' and 'await'
async def random_sleep(counter):
    delay = random.random() * 5
    print("{} sleeps for {:.2f} seconds".format(counter, delay))
    await asyncio.sleep(delay)
    print("{} awakens".format(counter))


@asyncio.coroutine
def five_sleepers():
    print("Creating five tasks")
    
    tasks = [
        asyncio.create_task(random_sleep(i)) for i in range(5)]
    
    print("Sleeping after starting five tasks")
    yield from asyncio.sleep(2)
    print("Waking and waiting for five tasks")
    yield from asyncio.wait(tasks)

asyncio.get_event_loop().run_until_complete(five_sleepers())
print("Done five tasks")


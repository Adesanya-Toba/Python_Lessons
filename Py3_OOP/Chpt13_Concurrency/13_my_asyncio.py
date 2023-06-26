import asyncio
import random


# New since python 3.8: use 'async def' and 'await'
async def random_sleep(counter):
    delay = random.random() * 5
    print(f"Task {counter} sleeps for {delay:.2f} seconds")
    await asyncio.sleep(delay)
    print(f"Task {counter} awakens, refreshed")


# Old method
# @asyncio.coroutine
# def five_sleepers():
#     print("Creating five tasks")
    
#     tasks = [
#         asyncio.create_task(random_sleep(i)) for i in range(5)]
    
#     print("Sleeping after starting five tasks")
#     yield from asyncio.sleep(2)
#     print("Waking and waiting for five tasks")
#     yield from asyncio.wait(tasks)

# asyncio.get_event_loop().run_until_complete(five_sleepers())
# print("Done five tasks")

# New method
async def sleepers(how_many:int = 5):
    print(f'Creating {how_many} tasks')
    tasks = [
        asyncio.create_task(random_sleep(i)) for i in range(how_many)]
    print(f'Waiting for {how_many} tasks')
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(sleepers(5))
    print('Done with the sleepers!')


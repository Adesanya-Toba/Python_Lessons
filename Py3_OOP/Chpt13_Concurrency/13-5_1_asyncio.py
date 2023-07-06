import asyncio
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(threadName)-11s [%(levelname)s]: %(message)s')
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


# New since python 3.8: use 'async def' and 'await'
async def random_sleep(counter):
    delay = random.random() * 5
    logger.info(f"Task {counter} sleeps for {delay:.2f} seconds")
    await asyncio.sleep(delay)
    logger.info(f"Task {counter} awakens, refreshed")


# Old method
# @asyncio.coroutine
# def five_sleepers():
#     logger.info("Creating five tasks")
    
#     tasks = [
#         asyncio.create_task(random_sleep(i)) for i in range(5)]
    
#     logger.info("Sleeping after starting five tasks")
#     yield from asyncio.sleep(2)
#     logger.info("Waking and waiting for five tasks")
#     yield from asyncio.wait(tasks)

# asyncio.get_event_loop().run_until_complete(five_sleepers())
# logger.info("Done five tasks")

# New method
async def sleepers(how_many:int = 5):
    logger.info(f'Creating {how_many} tasks')
    tasks = [
        asyncio.create_task(random_sleep(i)) for i in range(how_many)]
    logger.info(f'Waiting for {how_many} tasks')
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(sleepers(5))

    # asyncio.run(random_sleep(5))
    logger.info('Done with the sleepers!')


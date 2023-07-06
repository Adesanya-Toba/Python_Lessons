'''
The multiprocessing library is designed for when CPU-intensive jobs need to
happen in parallel and multiple cores are available. 
Multiprocessing is not as useful when the processes spend a majority of their time
waiting on I/O (for example, network, disk, database, or keyboard), but it is the 
way to go for parallel computation.

The multiprocessing module spins up new operating system processes to do the 
work. This means there is an entirely separate copy of the Python interpreter running 
for each process.
'''
from multiprocessing import Process, cpu_count
import time
import os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(processName)-11s %(threadName)-11s [%(levelname)s]: %(message)s')
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

class MuchCPU(Process):
    def run(self):
        logger.info(f'OS PID: {os.getpid()}')

        s = sum(2*i+1 for i in range(100_000_000))

if __name__ == '__main__':
    logger.info(f'CPU count: {cpu_count()}')

    num = (i for i in range(10))
    # logger.info(list(num))
    workers = [MuchCPU() for f in range(cpu_count())]
    t = time.perf_counter()
    for p in workers:
        p.start()
    for p in workers:
        p.join()
    logger.info(f'Work took {time.perf_counter() - t:.3f} seconds')

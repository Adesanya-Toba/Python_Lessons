'''A thread is a sequence of Python byte-code instructions that may be interrupted and 
resumed. The idea is to create separate, concurrent threads to allow computation to 
proceed while the program is waiting for I/O to happen. 
'''
import time
import math
import random
from threading import Thread, Lock

THE_ORDERS = [
    'Reuben',
    'Ham and Cheese',
    'Monte Cristo',
    'Tuna Melt',
    'Cuban',
    'Grilled Cheese',
    'French Dip',
    'BLT',
]

class Chef(Thread):
    def __init__(self, name:str):
        super().__init__(name=name)
        self.total = 0

    def get_order(self):
        self.order = THE_ORDERS.pop(0)

    def prepare(self):
        '''Simulate doing a lot of work with BIG computation.
        '''
        start = time.monotonic()
        target = start + 1 + random.random()
        for i in range(1_000_000_000):
            self.total += math.factorial(i)
            if time.monotonic() >= target:
                break
        print(f'{time.monotonic():.3f} {self.name} made {self.order}')

    def run(self):
        while True:
            try:
                self.get_order()
                self.prepare()
            except IndexError:
                break # No more orders

Mo = Chef('Micheal')
Constantine = Chef('Constantine')

if __name__ == '__main__':
    random.seed(2)
    Mo.start()
    Constantine.start()
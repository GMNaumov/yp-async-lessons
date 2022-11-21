import time
import os

from multiprocessing import Process

def printer(name):
    time.sleep(50)
    print('Hi', name)

if __name__ == '__main__':
    p = Process(target=printer, args=('George',))
    p.start()
    print('Let\'s wait...')

    print('Parent PID:', os.getpid())
    print('Child PID', p.pid)
    p.join()
    
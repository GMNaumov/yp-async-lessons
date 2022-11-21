import time

from multiprocessing import Process

def printer(name):
    time.sleep(3)
    print('Hi', name)

if __name__ == '__main__':
    p = Process(target=printer, args=('Alice',))
    p.start()
    print('Let\'s wait...')
    p.join()
    
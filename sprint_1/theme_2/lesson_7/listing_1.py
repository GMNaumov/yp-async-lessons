import multiprocessing

from multiprocessing import Process

class Worker(Process):
    def __init__(self, func, func_args, queue):
        multiprocessing.Process.__init__(self)
        self.func = func
        self.func_args = func_args
        self.queue = queue

    def run(self):
        pool = multiprocessing.Pool(processes=1)
        pool_output = pool.apply(self.func, (*self.func_args,))
        pool.close()
        pool.join()
        self.queue.put(pool_output)
        
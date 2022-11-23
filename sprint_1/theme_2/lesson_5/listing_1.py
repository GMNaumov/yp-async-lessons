import multiprocessing

def custom_func(i):
    print('Call function for process: %s' %i)
    for j in range(0, i):
        print('Function output: %s' %j)

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=custom_func, args=(i,))
        process.start()
        process.join()
        
from concurrent.futures import ThreadPoolExecutor
from math import pow

data = range(1, 10)
pool_size = 5


def f1(item):
    return pow(item, 2)


def f2(data):
    result = 0
    for i in data:
        result += i

    return result


def worker(data):
    """
    Возведение всех элементов массива в квадрат и
    подсчёт суммы всех элементов
    """
    result = 0
    with ThreadPoolExecutor(max_workers=pool_size) as pool:
        temp = pool.map(f1, data, chunksize=2)
        for t in temp:
            result += t

    return result


if __name__ == '__main__':
    print(worker(data))

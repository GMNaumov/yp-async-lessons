def f1(data_d):
    result = 0
    for i in data_d:
        result += f2(i)

    return result


def f2(data_t):
    return data_t ** 2


if __name__ == '__main__':
    dt = range(1, 10)
    print(f1(dt))

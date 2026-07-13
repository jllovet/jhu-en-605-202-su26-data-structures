def sequence(start=0, step=1):
    x = start
    while True:
        x += step
        yield x


def take(iterator, n):
    acc = []
    try:
        for _ in range(n):
            acc.append(next(iterator))
        return acc
    except StopIteration:    
        return acc


a = (x ** 2 for x in sequence())
take(a, 10)
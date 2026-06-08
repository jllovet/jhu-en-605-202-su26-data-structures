def f(n):
    if n == 1:
        return True
    else:
        return False


def g(n):
    return n - 1


def rec(n: int):
    if (f(n) == False):
        print(n)
        return (rec(g(n)))
    return 0


def iterative(n):
    while not f(n):
        print(n)
        n = g(n)
    return 0

print("calling rec(10)")
rec(10)
print("calling iterative(10)")
iterative(10)
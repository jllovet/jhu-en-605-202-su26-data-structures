def gfib(f0, f1, n):
    if n == 0:
        return f0
    if n == 1:
        return f1
    if n > 1:
        return gfib(f0, f1, n-1) + gfib(f0, f1, n-2)


# Standard
print(gfib(0, 1, 1))
print(gfib(0, 1, 2))
print(gfib(0, 1, 3))
print(gfib(0, 1, 4))
print(gfib(0, 1, 5))
print(gfib(0, 1, 6))
print(gfib(0, 1, 7))
print(gfib(0, 1, 8))
print(gfib(0, 1, 9))
print(gfib(0, 1, 10))

print()
# Nonstandard
print(gfib(2, 5, 1))
print(gfib(2, 5, 2))
print(gfib(2, 5, 3))
print(gfib(2, 5, 4))
print(gfib(2, 5, 5))
print(gfib(2, 5, 6))
print(gfib(2, 5, 7))
print(gfib(2, 5, 8))
print(gfib(2, 5, 9))
print(gfib(2, 5, 10))
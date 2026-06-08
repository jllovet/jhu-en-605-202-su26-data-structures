def print_indent(depth, s):
    print(" " * depth, end="")
    print(s)

def a(m, n, depth=0):
    print_indent(depth, f"call a(m, n): a({m}, {n})")
    depth += 2
    if m == 0:
        print_indent(depth, f"in case: m == 0")
        print_indent(depth, f"return n + 1: {n}+1")
        return n + 1
    if m != 0 and n == 0:
        print_indent(depth, f"in case: m != 0 and n == 0")
        print_indent(depth, f"return a(m-1, 1): a({m-1}, 1)")
        return a(m-1, 1, depth)
    if m != 0 and n != 0:
        print_indent(depth, f"in case: m != 0 and n == 0")
        print_indent(depth, f"return a(m-1, a(m, n-1)): a({m}-1, a({m}, {n}-1))")
        return a(m-1, a(m, n-1, depth), depth)


print(a(2,2))

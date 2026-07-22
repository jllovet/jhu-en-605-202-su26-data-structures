def mystery_sort(A):
    L = len(A)
    C = []
    C.extend([None]*L)
    output = []
    output.extend([None]*L)
    for i, n in enumerate(A):
        sum = 0
        for j in A:
            if j < n:
                sum += 1
            C[i] = sum
    for i in C:
        output[C[i]] = A[i]
    for i, x in enumerate(output):
        if x is None:
            output[i] = output[i-1]
    return output

A = [3,7,3,5,8,2]
output = mystery_sort(A)

print(output)
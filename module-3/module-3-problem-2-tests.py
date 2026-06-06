def running_average(A=[1, 2, 3]):
    len_A = len(A)
    running = 0
    def avg(A, running, len_A):
        # Base case
        if len(A) == 0:
            return running
        # Recursive case
        running = running + A[0]/len_A
        return avg(A[1:], running, len_A)
    # Invoke recursive function
    return avg(A, running, len_A)


print(
    all([
        running_average(A=[3, 3, 3]) == 3.0,
        running_average(A=[1, 2, 3]) == 2.0,
        running_average(A=[10]) == 10.0,
        running_average(A=[0, 0, 0]) == 0.0,
        running_average(A=[5, 4]) == 4.5
    ])
)

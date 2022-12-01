def make_multiplication_table(n, m):
    return [[i*j for i in range(1, m+1)] for j in range(1, n+1)]

def print_multiplication_table(arr):
    for row in arr:
        print(*row, sep=' ')

arr = make_multiplication_table(10, 10)
print_multiplication_table(arr)
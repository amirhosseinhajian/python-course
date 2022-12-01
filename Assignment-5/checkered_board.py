def make_checkred_board(n, m):
    return [['#' if (j % 2 == 0 and i % 2 == 0) or (j % 2 != 0 and i % 2 != 0) else '*' for i in range(m)] for j in range(n)]

def print_checkred_board(arr):
    for row in arr:
        print(*row, sep='')

arr = make_checkred_board(4, 10)
print_checkred_board(arr)
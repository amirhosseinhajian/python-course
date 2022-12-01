def make_diamond(n):
    return [int((n*2 - i) / 2) * ' ' + i * '*' for i in range(1, n*2, 2)] + [int((n*2 - i) / 2) * ' ' + i * '*' for i in range(n*2-3, 0, -2)]

try:
    arr = make_diamond(int(input("Enter number of rows: ")))
    print(*arr, sep="\n")
except:
    print("input number most be an integer.")
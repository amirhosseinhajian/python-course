def make_khayyam_pascal_triangle(n):
    arr = [[1 if (i==j or i==0) else 0 for i in range(j+1)] for j in range(n)]
    for row_index, row in enumerate(arr):
        for col_index, number in enumerate(row):
            if number == 0:
                arr[row_index][col_index] = arr[row_index-1][col_index] + arr[row_index-1][col_index-1]
    return arr

def print_khayyam_pascal_triangle(array):
    for row in array:
        print(*row, sep=" ")
try:
    khayyam_pascal_triangle = make_khayyam_pascal_triangle(int(input("Enter number of rows: ")))
    print_khayyam_pascal_triangle(khayyam_pascal_triangle)
except:
    print("input number most be an integer.")
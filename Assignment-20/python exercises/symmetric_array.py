def is_symmetric_array(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[-(i+1)]:
            return False
    return True

#---------------- TEST ----------------# 
array = [20, 1, 5, 5, 1, 20]
if is_symmetric_array(array):
     print("The array is symmetric") 
else:
    print("The array is not symmetric")

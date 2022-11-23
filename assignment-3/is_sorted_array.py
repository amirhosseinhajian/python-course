def convert_to_numeric_array(array):
    splited_array = array.split(" ")
    return [int(number) for number in splited_array]

def is_sorted_array(array):
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                return False
    return True

user_input = input("Enter the array with one space between each number: ")
user_input_array = convert_to_numeric_array(user_input)
if is_sorted_array(user_input_array):
    print("sorted")
else:
    print("not sorted")
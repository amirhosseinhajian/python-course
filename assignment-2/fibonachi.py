def fibonachi(element_number):
    if element_number == 1 or element_number == 2:
        return 1
    return fibonachi(element_number - 1) + fibonachi(element_number - 2)

try:
    for i in range(1, int(input("please enter the number of element: ")) + 1):
        print(fibonachi(i), "")
except:
    print("oops! input must be a number")
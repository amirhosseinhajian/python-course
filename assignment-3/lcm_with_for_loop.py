def find_greater(num1, num2):
    return num1 if num1 > num2 else num2

def lcm(num1, num2):
    greater_number = find_greater(number_1, number_2)
    for i in range(greater_number, num1 * num2 + 1):
        if i % num1 == 0 and i % num2 == 0:
            return i

if __name__ == '__main__':
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the seccond number: "))
    print(lcm(number_1, number_2))
    
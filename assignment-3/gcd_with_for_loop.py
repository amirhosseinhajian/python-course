def find_smaller_number(num1, num2):
    return num1 if num1 < num2 else num2

def gcd(num1, num2):
    smaller_number = find_smaller_number(num1, num2)
    for i in range(smaller_number, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i

if __name__ == '__main__':
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the seccond number: "))
    print(gcd(number_1, number_2))
import operator
import math

basic_operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
}

trigonometric_operators = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "cot": math.atan,
}

advance_operators = {
    "sqrt": math.sqrt,
    "fact": math.factorial,
}

def calculation_of_basic_operators(number1, operator, number2):
    return basic_operators[operator](number1, number2)

def calculation_of_trigonometric_operators(number, operator):
    return trigonometric_operators[operator](math.radians(number))

def calculation_of_advance_operators(number, operator):
    return advance_operators[operator](number)

def is_float(number):
    return number if number-math.floor(number) > 0 else int(number)

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

while True:
    try:
        print("-------------------------------")
        print("Welcom to the calculator program")
        number1 = float(input("please enter the number: "))
        number1 = is_float(number1)
        print("-------------------------------")
        print("please select operator")
        print("-------------------------------")
        print("sum: +")
        print("sub: -")
        print("mul: *")
        print("div: /")
        print("mod: %")
        print("sqrt: sqrt")
        print("sin: sin")
        print("cos: cos")
        print("tan: tan")
        print("cot: cot")
        print("factoriel: fact")
        operator =  input("operator: ")
        print("-------------------------------")

        if(operator in basic_operators):
            number2 = float(input("please enter the seccond number: "))
            number2 = is_float(number2)
            print(f"{bcolors.OKGREEN}{number1} {operator} {number2} =", is_float(calculation_of_basic_operators(number1, operator, number2)), bcolors.ENDC)
        
        elif(operator in trigonometric_operators):
            print(f"{bcolors.OKGREEN}{operator}({number1}) =", is_float(calculation_of_trigonometric_operators(number1, operator)), bcolors.ENDC)

        elif(operator in advance_operators):
            print(f"{bcolors.OKGREEN}{operator}({number1}) =", is_float(calculation_of_advance_operators(number1, operator)), bcolors.ENDC)
        
        else:
            print(bcolors.WARNING, "the entered operator doese not exist.", bcolors.ENDC)

    except:
        print("-------------------------------")
        print(bcolors.WARNING, "invalid input !!!!!!", bcolors.ENDC)

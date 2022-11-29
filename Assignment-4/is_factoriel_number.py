try: 
    number = int(input("Plese enter the number: "))
    accumulator = 1
    index = 1
    while accumulator < number:
        index += 1
        accumulator *= index
    print("yes") if accumulator == number else print("no")
except:
    print("Invalid input")
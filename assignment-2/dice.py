import random

while True:
    number = random.randint(1, 6)
    print(f"The number has turned: {number}")
    if number != 6:
        break
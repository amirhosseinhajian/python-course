import random

selected_numbers = []
n = 10
def generate_random_number(lower, upper):
    while True:
        random_number = random.randint(lower, upper)
        if random_number not in selected_numbers:
            selected_numbers.append(random_number)
            return random_number
    
random_numbers = [generate_random_number(1, 100) for i in range(n)]

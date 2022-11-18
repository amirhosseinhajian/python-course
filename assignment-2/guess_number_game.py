import random

random_number = random.randint(1, 30)
number_of_guess = 1
heart = 4

for i in range(heart):
    try:
        user_guess = int(input(f"you have {heart - i} chance. Please guess a number between 1 and 30: "))
        if user_guess == random_number:
            print(f"Congratulation! you won. the number of your guesses is {number_of_guess}.")
            break
        else:
            number_of_guess += 1
            print("go higher.", end=" ") if user_guess < random_number else print("go lower.", end=" ")
    except:
        print("input must be a number.")
else:
    print(f"Game over! the number was {random_number}.")
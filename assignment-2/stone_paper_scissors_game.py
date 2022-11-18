import random

def determining_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    if user_choice == "stone":
        return "user" if computer_choice == "scissors" else "computer"
    if user_choice == "paper":
        return "user" if computer_choice == "stone" else "computer"
    return "user" if computer_choice == "paper" else "computer"

def print_result(user_choice, computer_choice, result, user_score, computer_score):
    print("--------------------------------")
    print(f"your choice: {user_choice} and computer choice: {computer_choice}")
    if result == "draw":
        print("draw!")
    else:
        print(f"the winner is {result}.")
    print(f"your score: {user_score} AND computer score: {computer_score}")
    print("--------------------------------")

valid_choices = {
    "s": "stone",
    "p": "paper",
    "c": "scissors"
}
computer_score = 0
user_score = 0

while computer_score < 3 and user_score < 3:
    user_choice = input("please enter: s for stone, p for paper and c for scissors: ")
    if user_choice in list(valid_choices.keys()):
        user_choice = valid_choices[user_choice]
        computer_choice = random.choice(list(valid_choices.values()))
        result = determining_winner(user_choice, computer_choice)
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        print_result(user_choice, computer_choice, result, user_score, computer_score)
    else:
        print("invalid input.")
print(f"final winner is {'user' if user_score > computer_score else 'computer'}.")
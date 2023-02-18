from random import choice

choices = ["🤚", "✋"]
user_score = 0
cpu_1_score = 0
cpu_2_score = 0
for _ in range(5):
    while True:
        try:
            user_choice = choices[int(input("please Choose: 0 for 🤚 and 1 for ✋ "))]
            break 
        except:
            print("invalid input. Choose again.")
    cpu_1_choice = choice(choices)
    cpu_2_choice = choice(choices)
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"your choice: {user_choice} | cpu1 choice: {cpu_1_choice} | cpu2 choice {cpu_2_choice}")
    if user_choice == cpu_1_choice == cpu_2_choice:
        print("draw!")
    elif user_choice == cpu_1_choice:
        cpu_2_score += 1
    elif user_choice == cpu_2_choice:
        cpu_1_score += 1
    else:
        user_score += 1
    print(f"user score: {user_score} | cpu1 score: {cpu_1_score} | cpu2 score {cpu_2_score}")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
winner = ""
if user_score > cpu_1_score and user_score > cpu_2_score:
    winner = "user"
elif cpu_1_score > user_score and cpu_1_score > cpu_2_score:
    winner = "cpu 1"
elif cpu_2_score > user_score and cpu_2_score > cpu_1_score:
    winner = "cpu 2"
else:
    winner = False
if winner:
    print(f"The winner is the {winner}.")
else:
    print("No one has won!")
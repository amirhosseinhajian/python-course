total_scores = 0
number_of_scores = 0
while True:
    user_input = input("enter the score or enter exit for calculating the GPA: ")
    if user_input == "exit":
        break
    try:
        total_scores += float(user_input)
        number_of_scores += 1
    except:
        print("invalid input.")
try:
    print("GPA:", total_scores/number_of_scores)
except:
    print("GPA: 0")
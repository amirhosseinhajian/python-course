def average(array):
    return sum(array)/len(array)

def status(average):
    if average >= 17:
        return "Great"
    elif average < 17 and average >= 12:
        return "Normal"
    else:
        return "Fail"

def check_valid_score(score):
    return False if score < 0 or score > 20 else True

scores = []
name = input("please enter the student name: ")
family = input("please enter the student family: ")
i = 0
while i < 3:
    try:
        scores.append(float(input(f"please enter score {i+1}: ")))
        if not check_valid_score(scores[i]):
            i = i - 1
            scores.pop()
            print("score must be in range of 0-20")
        i = i + 1
    except:
        print("score must be float.")

average = average(scores)
status = status(average)

print(f"{name} {family}'s average is {average} and the status of this student is {status}. ")

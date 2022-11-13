def calculate_bmi(height, weight):
    return weight / height ** 2

def set_bmi_status(bmi):
    if bmi < 18.5:
        return"underweight"
    elif 18.5 <= bmi < 25:
        return "normal weight"
    elif 25 <= bmi < 30:
        return "overweight"
    elif 30 < bmi < 35:
        return "obese"
    elif bmi >= 35:
        return "clinically obese"

try:
    weight = float(input("please enter the weight(kg): "))
    height = float(input("please enter the height(m): "))
    bmi = calculate_bmi(height, weight)
    status = set_bmi_status(bmi)
    print(f"your bmi is {bmi} and your status is {status}.")
except:
    print("the input must be a float.")

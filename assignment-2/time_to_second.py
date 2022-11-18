def split_time(time):
    result = []
    for i in range(3):
        try:
            splited_section = time.split(":")[i]
            result.append(int(splited_section[1]) if splited_section[0] == "0" else int(splited_section)) 
        except:
            print("oops! input must be in form --:--:-- and should not contain characters.")
            exit()
    return result[0], result[1], result[2]

def is_valid_time_inputs(hour, minute, second):
    return False if hour < 0 or hour > 24 or minute < 0 or minute > 60 or second < 0 or second > 60 else True

def time2sec(hour, minute, second):
    return hour * 3600 + minute * 60 + second

hour, minute, second = split_time(input("enter the time: "))
if(not is_valid_time_inputs(hour, minute, second)):
    raise Exception("oops! The range of input numbers are invalid.")
print(f"result: {time2sec(hour, minute, second)}")

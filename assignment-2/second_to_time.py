def sec2time(second):
    hour = second // 3600
    minute = (second % 3600) // 60
    second = second % 3600 % 60 
    return hour, minute, second

def structuring_time(hour, minute, second):
    return (str(hour) if hour > 10 else "0" + str(hour)) + ":" + (str(minute) if minute > 10 else "0" + str(minute)) + ":" + (str(second) if second > 10 else "0" + str(second))

try:
    second = int(input("plese enter the second: "))
    hour, minute, second = sec2time(second)
    time = structuring_time(hour, minute, second)
    print("result: ", time)
except:
    print("the input must be a number.")

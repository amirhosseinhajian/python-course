class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.fix()

    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)
    
    def sum(self, other_time):
        s_new = self.second + other_time.second
        m_new = self.minute + other_time.minute
        h_new = self.hour + other_time.hour
        return Time(h_new, m_new, s_new)

    def sub(self, other_time):
        s_new = self.second - other_time.second
        m_new = self.minute - other_time.minute
        h_new = self.hour - other_time.hour
        return Time(h_new, m_new, s_new)

    def fix(self):
        while self.second >= 60:
            self.second -= 60
            self.minute += 1
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        while self.second < 0:
            self.second += 60
            self.minute -= 1
        while self.minute < 0:
            self.minute += 60
            self.hour -= 1

    @staticmethod
    def second_to_time(second):
        hour = int(second / 3600)
        minute = int((second % 3600) / 60)
        second = int(second % 60)
        return Time(hour, minute, second)
    
    @staticmethod
    def time_to_second(time):
        return time.hour * 3600 + time.minute * 60 + time.second

    @staticmethod
    def gmt_to_tehran(time):
        minute = time.minute + 30
        hour = time.hour + 3
        if minute > 60:
            minute -= 60
            hour += 1
        if hour > 23:
            hour %= 24
        return Time(hour, minute, time.second)

##### TEST CASE #####
t1 = Time(12, 47, 54)
t2 = Time(1, 45, 19)
print("t1 = ", end=" ")
t1.show()
print("t2 = ", end=" ")
t2.show()
print("sum:", end=" ")
t1.sum(t2).show()
print("sub:", end=" ")
t1.sub(t2).show()
print("second to time of 6010:", end=' ')
Time.second_to_time(6010).show()
print(f"time to second of t1:", Time.time_to_second(t1))
print("GMT to tehran of (22: 45: 31) =", end=" ")
Time.gmt_to_tehran(Time(22, 45, 31)).show()
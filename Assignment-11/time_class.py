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

    def second_to_time(self, second):
        hour = int(second / 3600)
        minute = int((second % 3600) / 60)
        second = int(second % 60)
        return Time(hour, minute, second)
    
    def time_to_second(self, time):
        return time.hour * 3600 + time.minute * 60 + time.second

    def gmt_to_tehran(self, time):
        minute = time.minute + 30
        hour = time.hour + 3
        if minute > 60:
            minute -= 60
            hour += 1
        if hour > 23:
            hour %= 24
        return Time(hour, minute, time.second)

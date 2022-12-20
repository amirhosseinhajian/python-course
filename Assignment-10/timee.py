class Time:
    def __init__(self, seconds, minute, hour):
        self.seconds = seconds
        self.minute = minute
        self.hour = hour
        self.check_valid_inputs()
    
    def check_valid_inputs(self):
        ...

    def sum(self, other_time):
        ...

    def sub(self, other_time):
        ...
    
    def time_to_seconds(self, time):
        ...
    
    def seconds_to_time(self, seconds):
        ...

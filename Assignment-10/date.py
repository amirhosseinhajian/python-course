class Date:
    def __init__(self, day, month, year, hour, minute, seconds):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
        self.seconds = seconds
        self.check_valid_inputs()
        
    def check_valid_inputs():
        ...
    
    def sum(self, other_date):
        ...
    
    def sub(self, other_date):
        ...
    
    def convert_to_shamsi_date(self, date):
        ...

    def convert_to_miladi_date(self, date):
        ...
    
    def convert_to_ghamari_date(self, date):
        ...
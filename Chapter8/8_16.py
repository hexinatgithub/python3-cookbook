import time


class Date:
    def __init__(self, year, month, day):
        # Primary constructor
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        # Alternate constructor
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


class NewDate(Date):
    pass


c = Date.today()  # Creates an instance of Date (cls=Date)
d = NewDate.today()  # Creates an instance of NewDate (cls=NewDate)

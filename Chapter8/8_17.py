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


d = Date.__new__(Date)

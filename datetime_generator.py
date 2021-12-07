import datetime
import random


class RandomDateTime:
    def __init__(self, start_dt, end_dt, pattern_dt):
        self.start_dt = datetime.datetime.strptime(start_dt, pattern_dt)
        self.end_dt = datetime.datetime.strptime(end_dt, pattern_dt)
        self.pattern_dt = pattern_dt

    def random_dt(self):
        milliseconds = (self.end_dt - self.start_dt).total_seconds() * 1000
        random_milliseconds = random.randrange(int(milliseconds))
        return (self.start_dt + datetime.timedelta(milliseconds=random_milliseconds)).strftime(self.pattern_dt)

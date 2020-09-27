import time


class Transaction(object):
    def __init__(self, string):
        self.timestamp = time.time()
        self.string = string

    def __str__(self):
        return self.string
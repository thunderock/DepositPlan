from utils import transaction


class UserLog(object):
    """:arg
    class to maintain user deposit logs"""

    def __init__(self):
        self.__transactions = []

    def write_transaction(self, string):
        t = transaction.Transaction(string)
        self.__transactions.append(t)

    def print_transactions(self, sort=True):
        if sort:
            transactions = sorted(self.__transactions, key=lambda x: x.timestamp)
        for transaction in transactions:
            print(transaction)

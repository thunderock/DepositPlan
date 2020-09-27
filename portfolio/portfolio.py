from utils import log
from abc import abstractmethod


class PortFolio(object):
    """:arg
    portfolio base class"""

    name = 'general_portfolio'

    @property
    @abstractmethod
    def name(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(PortFolio, self).__init__(*args, **kwargs)
        self.__current_amount = 0

    @property
    def current_amount(self):
        return self.__current_amount

    def increment_current_amount(self, val):
        self.__current_amount += val
        return True

    def decrement_current_amount(self, val):
        if val > self.__current_amount:
            return False
        self.__current_amount -= val
        return True

    def __str__(self):
        return "{0} : {1}".format(self.name, self.__current_amount)




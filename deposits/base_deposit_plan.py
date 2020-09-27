import sys
from abc import abstractmethod
from utils import log


class DepositPlan(object):
    """:arg
    base deposit plan"""

    def __init__(self, name='base_deposit_plan', portfolios=[], denominations=[], times_transfer_possible=sys.maxsize, *args, **kwargs):
        super(DepositPlan, self).__init__(*args, **kwargs)
        self.__portfolios = portfolios
        self.__denominations = denominations
        self.__times_transfer_possible = times_transfer_possible
        self.__transfers_made = 0
        self.name = name

    @property
    def minimum_possible_denomination(self):
        return sum(self.__denominations)

    def transfer_possible(self):
        return self.__transfers_made < self.__times_transfer_possible

    def transfer_fund(self):
        self.__transfers_made += 1
        for index in range(len(self.__denominations)):
            self.__portfolios[index].increment_current_amount(self.__denominations[index])

    @property
    def portfolio_balance(self):
        ret = {}
        # Assumption: there can be multiple same time of portfolios
        # in a deposit plan
        for portfolio in self.__portfolios:
            if portfolio.name in ret:
                ret[portfolio.name] += portfolio.current_amount
            else:
                ret[portfolio.name] = portfolio.current_amount
        return ret

    @property
    @abstractmethod
    def portfolios(self):
        return self.__portfolios




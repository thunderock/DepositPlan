from user import user_log
from utils import log, algorithms, transaction


class User(object):
    def __init__(self, deposit_plans=[]):
        self.__deposit_plans = deposit_plans
        self.__user_log = user_log.UserLog()

    def add_deposit_plan(self, deposit_plan):
        self.__deposit_plans.append(deposit_plan)

    def __is_fund_deposit_possible(self, amount):
        # amount deposited should be either equal to one of plans
        # value or both of them
        # for a portfolio in which amount can be deposited multiple times
        # those amounts cannot be part of same fund deposit
        return algorithms.subset_sum(
        [i.minimum_possible_denomination if i.transfer_possible else 0
        for i in self.__deposit_plans],
            amount)

    def deposit_fund(self, amount):
        masks = self.__is_fund_deposit_possible(amount)
        if not any(masks):
            log.logger.warning("can't deposit this amount")
            return False

        for idx in range(len(masks)):
            mask = masks[idx]
            if mask:

                deposit_plan = self.__deposit_plans[idx]
                self.__user_log.write_transaction("deposit amount:  {0}".format(amount))
                deposit_plan.transfer_fund()
        return True

    def print_transactions(self):
        print("PRINTING TRANSACTIONS ")
        self.__user_log.print_transactions()

    def print_portfolio_balance(self):

        print("PRINTING PORTFOLIO BALANCE ")
        portfolios = set()
        for deposit_plan in self.__deposit_plans:
            for portfolio in deposit_plan.portfolios:
                portfolios.add(portfolio)

        for portfolio in portfolios:
            print(portfolio)

from user import user
from portfolio import high_risk, retirement, portfolio
from deposits import base_deposit_plan
from utils import log
from config import config
import sys


log.setup_logging()


class Engine(object):
    """:arg
    abstraction driver for internal components,
    all assertions here, not with components
    """
    __instance = None

    def __init__(self):
        if Engine.__instance:
            raise Exception("can't have any other instance of Engine class")
        self.__users = None
        self.__config = config.Config("deposit_plan")
        self.__supported_portfolios = {portfolio.name: portfolio for portfolio in
                                       [high_risk.HighRiskPortFolio(), retirement.RetirementPortFolio()]}
        self.__supported_deposits = ['one_time', 'monthly']
        log.set_logger(self.__config.get("app_name", str))
        Engine.__instance = self

    def add_user(self):
        return user.User()
    
    def get_portfolio(self, string):
        assert string in self.__supported_portfolios, \
            "only {0} are supported".format(self.__supported_portfolios.keys())
        return self.__supported_portfolios[string]
        
    def add_deposits(self, string, user_object, portfolios, denominations):
        assert isinstance(portfolios, list), "portfolios is expected to be a list"
        for p in portfolios:
            assert isinstance(p, portfolio.PortFolio), "portfolio are required to be added to deposit"
        assert isinstance(user_object, user.User), "deposits can be added to a user only"
        assert string in self.__supported_deposits, \
            "only {0} are supported".format(self.__supported_deposits.keys())
        assert len(portfolios) == len(denominations), "size of denominations should be equal to portfolios"
        deposit_plan = base_deposit_plan.DepositPlan(
            name=string,
            portfolios=portfolios,
            times_transfer_possible=1 if string == 'one_times' else sys.maxsize,
            denominations=denominations
        )
        user_object.add_deposit_plan(deposit_plan)

    @staticmethod
    def deposit_money(user_object, amount):
        assert isinstance(user_object, user.User), "money can be deposited for a user"
        is_possible = user_object.deposit_fund(amount=amount)
        info = "money deposited " if is_possible else "money could not be deposited"
        print(info)
        log.logger.warning(info)

    @staticmethod
    def print_portfolio_balance(user_object):
        assert isinstance(user_object, user.User), "portfolio balance can be checked only for a user"
        user_object.print_portfolio_balance()

    @staticmethod
    def print_transactions(user_object):
        assert isinstance(user_object, user.User), "transactions can only be checked for a user"
        user_object.print_transactions()


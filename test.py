# script to test functional requirements

from user import user
from portfolio import high_risk, retirement
from deposits import base_deposit_plan
from utils import log
from config import config

log.setup_logging()
log.set_logger("test")
from utils.log import logger

logger.warning("starting testing")

conf = config.Config('test')

portfolio1 = high_risk.HighRiskPortFolio()
portfolio2 = retirement.RetirementPortFolio()


deposit_plan1 = base_deposit_plan.DepositPlan(
    name='one_time',
    portfolios=[portfolio1, portfolio2], 
    times_transfer_possible=1,
    denominations=[10000, 500]
)

deposit_plan2 = base_deposit_plan.DepositPlan(
    name='monthly',
    portfolios=[portfolio1, portfolio2],
    denominations=[0, 100]
)


u1 = user.User(deposit_plans=[deposit_plan1, deposit_plan2])

# transaction 1
deposit_possible = u1.deposit_fund(amount=10500)
if deposit_possible: print("deposit is possible")


# transaction 2
deposit_possible = u1.deposit_fund(amount=100)
if deposit_possible: print("deposit is possible")

u1.print_transactions()


# transaction 3
deposit_possible = u1.deposit_fund(amount=300)

if deposit_possible: print("deposit is possible")


# transaction 4
deposit_possible = u1.deposit_fund(amount=100)
if not deposit_possible: print("deposit is not possible")

u1.print_portfolio_balance()




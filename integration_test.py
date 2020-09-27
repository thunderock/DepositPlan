from engine import engine

e = engine.Engine()

user1 = e.add_user()
high_risk_portfolio = e.get_portfolio("high_risk_portfolio")
retirement_portfolio = e.get_portfolio("retirement_portfolio")
e.add_deposits("monthly", user1,
               portfolios=[high_risk_portfolio, retirement_portfolio],
               denominations=[10000, 500])

e.add_deposits("one_time", user1,
               portfolios=[high_risk_portfolio, retirement_portfolio],
               denominations=[0, 100])

e.deposit_money(user1, 10500)
e.deposit_money(user1, 100)

e.deposit_money(user1, 300)
e.print_portfolio_balance(user1)
e.print_transactions(user1)


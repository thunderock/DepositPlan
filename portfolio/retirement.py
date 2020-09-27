from portfolio import portfolio


class RetirementPortFolio(portfolio.PortFolio):

    name = 'retirement_portfolio'

    def __init__(self, *args, **kwargs):
        super(RetirementPortFolio, self).__init__(*args, **kwargs)

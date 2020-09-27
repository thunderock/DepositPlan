from portfolio import portfolio


class HighRiskPortFolio(portfolio.PortFolio):
    name = 'high_risk_portfolio'

    def __init__(self, *args, **kwargs):
        super(HighRiskPortFolio, self).__init__(*args, **kwargs)

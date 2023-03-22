class FundingRound:
    
    all = []
    
    def __init__(self, startup, venture_capitalist, investment_type, investment):
        self.startup = startup
        self.venture_capitalist = venture_capitalist
        self.type = investment_type
        self.investment = investment
        self.all.append(self)
        
    
    
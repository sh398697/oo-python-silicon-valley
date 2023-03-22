from .funding_round import FundingRound

class VentureCapitalist:
    
    all = []
    tres_commas_club = []
    
    def __init__(self, name, net_worth):
        self.name = name
        self.net_worth = net_worth
        
        VentureCapitalist.all.append(self)
        
        if net_worth > 1000000:
            VentureCapitalist.tres_commas_club.append(self)


    @property
    def funding_rounds(self):
        return [fr for fr in FundingRound.all if fr.venture_capitalist == self]
    
    @property
    def num_funding_rounds(self):
        
        total_funding_rounds = 0

        for funding_round in FundingRound.all:
            if funding_round.venture_capitalist == self:
                total_funding_rounds += 1

        return total_funding_rounds


    @property
    def portfolio(self):
        return list({fr.startup for fr in self.funding_rounds})

    @property
    def startup_roster(self):
        return list({fr.startup.name for fr in self.funding_rounds})

    def offer_contract(self, startup, investment_type, investment_amount):
        
        FundingRound(self, investment_type, investment_amount)
        
        self.num_funding_rounds += 1
        
        if startup not in self.portfolio:
            self.portfolio.append(startup)
        if investment_amount > self.biggest_investment:
            self.biggest_investment = investment_amount


    @property
    def biggest_investment(self):
        big_investment_list = [fr.investment for fr in self.funding_rounds]
        big_investment_list.sort(reverse=True)
        return big_investment_list[0]


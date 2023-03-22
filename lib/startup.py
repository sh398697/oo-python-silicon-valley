from .funding_round import FundingRound

class Startup:
   
   all = []
   all_domains = []
   
   def __init__(self, name, founder, domain):
      self.name = name
      self._founder = founder
      self._domain = domain
      Startup.all.append(self)
      Startup.all_domains.append(self.domain)


   @property
   def founder(self):
      return self._founder


   @property
   def domain(self):
      return self._domain


   @property
   def num_funding_rounds(self):
      
      num_fund_rds = 0
      
      for funding_round in FundingRound.all:
         if funding_round.startup == self:
            num_fund_rds += 1
      
      return num_fund_rds


   @property
   def total_funds(self):

      total_fnds = 0

      for funding_round in FundingRound.all:
         if funding_round.startup == self:
               total_fnds += funding_round.investment

      return total_fnds

 
   @property
   def investors(self):
      return list({fr.venture_capitalist.name for fr in FundingRound.all if fr.startup == self })


   @property
   def big_investors(self):

      big_investor_list = []

      for fr in FundingRound.all:
         if fr.startup == self and fr.venture_capitalist.net_worth >= 1000000 and fr.venture_capitalist.name not in big_investor_list:
            big_investor_list.append(fr.venture_capitalist.name)

      return big_investor_list


   def pivot(self, name, domain):
      self.name = name
      self._domain = domain


   def sign_contract(self, venture_capitalist, contract_type, contract_amount):
      FundingRound(self, venture_capitalist, contract_type, contract_amount)


   @classmethod
   def find_by_founder(cls, founder):
      for startup in cls.all:
         if startup._founder == founder:
            return(f"{startup.founder}: {startup.name}")

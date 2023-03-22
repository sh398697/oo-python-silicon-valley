from lib import *

# code here
# e.g.
s1 = Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
s2 = Startup( 'Scott Industries', 'Scott Henry', 'www.scott.com' )

vc1 = VentureCapitalist( 'Peter Gregory', 90000000 )
vc2 = VentureCapitalist( 'Austin Henry', 200000000 )

#fr1 = FundingRound( s2, vc2, 'Pre-Seed', 200000.99 )

s1.sign_contract(vc1, "seed", 20)
s2.sign_contract(vc2, "pre-seed", 10)


def print_s1_and_vc1():
    print("Here's the info on s1:")
    print(f"Name: {s1.name}")
    print(f"Founder: {s1._founder}")
    print(f"Domain: {s1.domain}")
    print(f"Number of funding rounds: {s1.num_funding_rounds}")
    print(f"Total Funding: {s1.total_funds}")
    print(f"Investors: {s1.investors}")
    print(f"Big Investors: {s1.big_investors}")

    print('')

    print("Here's the info on vc1:")
    print(f"Name: {vc1.name}")
    print(f"Total Worth: {vc1.net_worth}")
    print(f"Number of funding rounds: {vc1.num_funding_rounds}")
    print(f"Portfolio: {vc1.startup_roster}")
    
    # FINISH ME!
    print(f"Biggest Investment: {vc1.biggest_investment}")
    print('')

print_s1_and_vc1()
print('')
print("Doing another found of funding")
s1.sign_contract(vc1, "second round", 2000000)
s2.sign_contract(vc2, "first round", 1000000)

print_s1_and_vc1()

# do not remove
import ipdb; ipdb.set_trace()

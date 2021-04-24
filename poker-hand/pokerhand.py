from collections import defaultdict

def score(hand):
    ranks = '2345678910JQKA'
    cards = hand[0].split(',')
    rcounts = defaultdict(int)
    for card in cards:
        rank = card[:-1]
        rcounts[rank] += 1
    sortedranks = {k: v for k, v in sorted(rcounts.items(),key=lambda item: item[1],reverse=True)}

    print(sortedranks)
       


score(['AS, 10C, 10H, 3D, 3S'])
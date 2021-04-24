from collections import defaultdict

# Function to determine the number of occurences in one hand for each card
def score(hand):
    ranks = '23456789TJQKA'
    handBasicType = 'n'
    cards = ''.join(hand[0].split())
    cards = cards.split(',')
    rcounts = defaultdict(int)
    score = defaultdict(int)
    for card in cards:
        rank = card[:-1]
        if rank.isalpha() == True:
            rcounts[ranks.find(rank)+1]+=1
        else:
            rcounts[int(rank)] += 1
        suit = card[-1]
        score[suit] += 1
    ranks = sorted(rcounts.items(),reverse=True)
    
#score(['AS, 10C, 10H, 3D, 3S'])
print(score(['AS, 10S, 9S, 3S, 4S']))
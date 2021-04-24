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

    # Determines if hand is a flush
    if len(score) == 1:
        print("Hand is a flush")
        if ranks[0][0] == ranks[1][0]+1:
            handBasicType = 'Straight Flush'
        else:
            handBasicType = 'Flush'
        return score, handBasicType
    
#score(['AS, 10C, 10H, 3D, 3S'])
print(score(['AS, 10S, 9S, 3S, 4S']))
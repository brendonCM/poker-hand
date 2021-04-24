from collections import defaultdict

# Function to determine the number of occurences in one hand for each card
def ranksAndScore(hand):
    ranks = '23456789TJQKA'
    cards = ''.join(hand[0].split())
    cards = cards.split(',')
    rcounts = defaultdict(int)
    scounts = defaultdict(int)
    for card in cards:
        rank = card[:-1]
        if rank.isalpha() == True:
            rcounts[ranks.find(rank)+1]+=1
        else:
            rcounts[int(rank)] += 1
        suit = card[-1]
        scounts[suit] += 1
    ranks = sorted(rcounts.items(),reverse=True)
    suites = sorted(scounts.items(),reverse=True)
    return ranks, suites

def typePokerHand(ranks, suits):

        # Determines if hand is flush
    if len(suits) == 1:
        if ranks[0][0] == ranks[1][0]+1:
            handBasicType = 'Straight Flush'
        else:
            return 'Flush'

    # Determines if hand is straight
    if len(ranks) == 5:
        if ranks[0][0] - ranks[4][0] == 4:
            return 'Straight'
        else:
            return 'High Card'
    
    # Determines the type of kind for the hand
    if len(ranks) == 2:
        if ranks[0][1] == 4 and ranks[1][0] == 'J':
            return 'Five of a kind'
        elif ranks[0][1] == 3 and ranks[1][1] == '2':
            return 'Full House'
        else:
            return 'Four of a kind'

    if len(ranks) == 3:    
        if ranks[0][1] == 3 and ranks[1][1] == 1 and ranks[2][1] == 1:
            handBasicType = 'Three of a kind'
            return handBasicType
        elif ranks[0][1] == 2 and ranks[1][1] == 2 and ranks[2][1] == 1:
            return 'Two Pair'

    if len(ranks) == 4:
        if ranks[0][1] == 2 and ranks[1][1] == 1 and ranks[2][1] == 1 and ranks[3][1] == 1:
            return 'One Pair'

def poker(hand):
    hands = [[hand,ranksAndScore(hand),""]]
    hands[0][2] = typePokerHand(hands[0][1][0],hands[0][1][1])

poker(['10S, 10H, 8S, 7H, 4C'])
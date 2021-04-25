from collections import defaultdict

# Function to determine the number of occurences in one hand for each card
def ranksAndSuits(hand):
    ranks = '23456789TJQKA'
    cards = ''.join(hand[0].split())
    cards = cards.split(',')
    rcounts = defaultdict(int)
    scounts = defaultdict(int)
    for card in cards:
        rank = card[:-1]
        suit = card[-1]
        if rank.isalpha() == True:
            rcounts[ranks.find(rank)+2]+=1
        else:
            rcounts[int(rank)] += 1
        scounts[suit] += 1
    ranks = sorted(rcounts.items(),reverse=True)
    suits = sorted(scounts.items(),reverse=True)
    return ranks, suits


def typePokerHand(ranks, suits):

    # Determines if hand is flush
    if len(suits) == 1:
        if ranks[0][0] == ranks[1][0]+1:
            return 'Straight Flush'
        else:
            return 'Flush'

    # Determines if hand is straight
    if len(ranks) == 5:
        if ranks[0][0] - ranks[4][0] == 4:
            return 'Straight'
        else:
            return 'High Card'
    
    # Determines the type of kind for the hand and Pair
    if len(ranks) == 2:
        if ranks[0][1] == 4 and ranks[1][0] == 'J':
            return 'Five of a kind'
        elif ranks[0][1] == 3 and ranks[1][1] == 2:
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

    return 'Not a proper poker hand'
    
def poker(hand):
    type_hands = [hand,ranksAndSuits(hand)]
    type_hands.append(typePokerHand(type_hands[1][0],type_hands[1][1]))
    return type_hands[2]

#Expected output is High Card
print(poker(['KD, QD, 7S, 4S, 3H']))

#Expected output is Two Pair
print(poker(['JH, JS, 3C, 3S, 2H']))

#Expected output is Flush
print(poker(['JD, 9D, 8D, 4D, 3D']))

#Expected output is Four of a kind
print(poker(['2D, 5C, 5D, 5H, 5S']))

#Expected output is a Full House
print(poker(['8D, 7C, 8H, 7H, 8S']))

#Expected out is not a proper poker hand
print(poker(['8D, 8C, 8H, 8H, 8S']))

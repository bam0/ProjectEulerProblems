'''
Problem: How many hands does Player 1 win (in the following
set of poker hands)?

This is the type of problem that 100 people will give 100 very different
solutions to. The following solution will simply be one of a plethora of
solutions. Since each approach can be rather lengthy, I've decided to focus
on just one here.
Before we jump into the meat of it, let's read the file and generate all of
the hands for player 1 and player 2.
'''
with open('poker_hands', 'r') as hands:
    p1, p2 = [], []
    hand = hands.readline().strip().split()
    while(hand):
        p1.append(hand[:5])   # p1 gets first 5 cards
        p2.append(hand[5:])   # p2 gets last 5 cards
        hand = hands.readline().strip().split()
'''
Now we'll create a list of values from 2 to 14 in a dictionary indicating the 
relative values on each card. 
'''
values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
for i in range(2, 10):
    values[str(i)] = i
'''
The following helper function checks to see if the values in a hand are all 
consecutive, which would indicate a straight. 
'''
def check_consec(val_lst):
    for i in range(4):
        if val_lst[i] != val_lst[i+1]-1:
            return False
    return True
'''
And the next helper function will be used frequently in calculating a hand's score.
Its purpose will be to take in a Counter of each value in the hand, and return a descending
list in order of frequency and value.  
'''
def sort_me(c):
    return sorted(c.items(), key=lambda x: x[1], reverse=True)
'''
Now we can go ahead and write a function that will attach a score to each hand. Scores will 
range from 1-10 in the order designated in the problem. For breaking ties, we will also 
attach either the sorted list of values, or the value of sort_me depending on whether the
latter is necessary.  
'''
from collections import Counter
def calc_score(cards):
    suits = set(card[1] for card in cards)
    vals = sorted(values[card[0]] for card in cards)
    if len(suits) == 1:                    # Check if cards are all same suit (flush)
        if  vals == [10, 11, 12, 13, 14]:  # Check for royal flush
            return (10,)
        elif check_consec(vals):           # Check for straight flush
            return (9, vals)
        return (6, vals)                   # Guaranteed at least a flush
    group = Counter(vals)
    mx_val = max(group.values())
    if len(group) == 2:
        if mx_val == 4:                    # Check for four of a kind
            return (8, sort_me(group))
        return (7, sort_me(group))         # Otherwise we have a Full House
    if check_consec(vals):                 # Check for regular Straight
        return (5, vals)
    if mx_val == 3:                        # Check for three of a kind
        return (4, sort_me(group))
    if len(group) == 3:                    # Check for two pairs
        return (3, sort_me(group))
    if mx_val == 2:                        # Check for one pair
        return (2, sort_me(group))
    return (1, vals[::-1])                 # Else we can only compare highest card
'''
While the previous function contains a good bit of code that can be cleaned up and 
written in a more concise way, it should demonstrate each check clearly. 
Finally we just need to write a couple more functions to arrive at the solution. 
The following takes in two hands and returns the winner. 
'''
def comp_hands(p_one, p_two):
    return calc_score(p_one) > calc_score(p_two)
'''
And lastly, we find the total wins by player 1. 
'''
def solution():
    return sum(comp_hands(p1[i], p2[i]) for i in range(len(p1)))

print('Number of wins:', solution())  # Number of wins: 376

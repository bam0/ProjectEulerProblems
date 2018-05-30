'''
Problem: How many different ways can £2 be made using any number of coins?
(1, 2, 5, 10, 20, 50, 100, 200) pence

Although this is a problem you could ask anyone on the street, it can be
a serious challenge to puzzle over. How can you stay organized and make sure
all coin combinations 1) work, and 2) are distinct.
When I was thinking about this problem originally, I was convinced the best solution
would be recursive. So I set out on making it a reality. Using a list of values
representing the number used of each coin, and an integer representing the amount of
money you currently have, I made the following solution.
It's definitely not for the feint of heart, though, so be warned:
'''
def find_200(L, s):     # Takes in a list of the amount of each coin, and s is the sum
    t = 0               # Initialize the total
    if s == 200:        # Sum is 200, so stop
        return 1
    if s == 0:
        t += find_200([L[0]+1]+L[1:], 200)             # Add 1 to the 200 coin
    if sum(L[2:])== 0 and s <= 100:
        t += find_200(L[:1]+[L[1]+1]+L[2:], s + 100)   # Add 1 to the 100 coin
    if sum(L[3:]) == 0 and s <= 150:
        t += find_200(L[:2]+[L[2]+1]+L[3:], s + 50)    # Add 1 to the 50 coin
    if sum(L[4:]) == 0 and s <= 180:
        t += find_200(L[:3]+[L[3]+1]+L[4:], s + 20)    # Add 1 to the 20 coin
    if sum(L[5:]) == 0 and s <= 190:
        t += find_200(L[:4]+[L[4]+1]+L[5:], s + 10)    # Add 1 to the 10 coin
    if sum(L[6:]) == 0 and s <= 195:
        t += find_200(L[:5]+[L[5]+1]+L[6:], s + 5)     # Add 1 to the 5 coin
    if sum(L[7:]) == 0 and s <= 198:
        t += find_200(L[:6]+[L[6]+1]+L[7:], s + 2)     # Add 1 to the 2 coin
    if s < 200:
        t += find_200(L[:7]+[L[7]+1], s + 1)           # Add 1 to the 1 coin
    return t         # Return the total
'''
The main issue with the previous solution, among many things, is that we keep 
having to reinitialize the list every time we want to call the function with a different
value in the list, due to the fact that lists are mutable. It doesn't help that the
recursive stack is also large due to all those if statements. 
All in all this solution is very inefficient and takes too long for comfort to produce
an answer (10s+). 
After consulting the pdf accompanying this problem, I felt like an absolute buffoon.
The optimal solution takes only a few lines of code to execute! All we need to do 
is use our friend dynamic programming.
First we initialize a list of size amount with 0's and one 1 to start off at index 0. 
Then we iterate over each coin in the coin list, adding the number of ways to get to
each position by the number of ways to get to the previous position, separated by that 
coin's value. This makes for quite the efficient solution!
'''
def optimal(cns, amt):                 # Take in a list of coins, and the target amount
    ways = [1] + [0]*(amt)             # Initialize the ways array with 0's
    for i in range(len(cns)):
        for j in range(cns[i], amt+1): # Iterate over each coin, stepping by the coin's value
            ways[j]+=ways[j-cns[i]]    # Add the number of ways separated by the coin's value
    return ways[amt]                   # Get the final total

def solution():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    amount = 200
    return optimal(coins, amount)

print('Number of ways:', solution())   # Number of ways: 73682

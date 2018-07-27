'''
Problem: How many different ways can one hundred be written as a sum of at
least two positive integers?

Imagine that instead of using just numbers, we are using coins. The problem would then
be asking, how many different ways can we make $1 using coins of denominations 1, 2, ... 99?
Luckily, we already developed a very efficient algorithm for this in problem 31.
'''
def optimal(cns, amt):                 # Take in a list of coins, and the target amount
    ways = [1] + [0]*(amt)             # Initialize the ways array with 0's
    for i in range(len(cns)):
        for j in range(cns[i], amt+1): # Iterate over each coin, stepping by the coin's value
            ways[j]+=ways[j-cns[i]]    # Add the number of ways separated by the coin's value
    return ways[amt]                   # Get the final total
'''
All we need to do is replace the coins list with [1, ..., 99] and set the amount to 100. 
'''
def solution(n):
    coins = [i for i in range(1, n)]
    return optimal(coins, n)
'''
This method gives us a result in less than 1 millisecond. But for larger values, we will need
to develop a different algorithm, as this one will run far too slowly.
This will be seen in problem 78. 
'''
print('Number of sums to 100:', solution(100))  # Number of sums to 100: 190569291

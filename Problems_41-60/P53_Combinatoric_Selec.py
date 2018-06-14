'''
Problem: How many, not necessarily distinct, values of  nCk,
for 1 ≤ n ≤ 100, are greater than one-million?

Conveniently for us, we already have a formula for evaluating nCk,
which was used in problem 15. So the simplest approach would just be to
iterate over all values of nCk for the given range of values of n.
'''
def n_Choose_k(n, k):
    result = 1
    for i in range(k):
        result*=(n-i)/(k-i)      # Taken from the formula n!/k!(n-k)!
    return int(result)

def solution1(n, m):
    count = 0
    for i in range(n+1):
        for j in range(i):
            if n_Choose_k(i, j) > m:  # Find the values greater than the given limit
                count += 1
    return count
'''
We can take this solution a step further by halving the number of values we have to 
check. Since nCk is the same as nC(n-k), we gain two values for the price of one. 
That is unless n is even, in which case we would need to check nCn/2.      
'''
def solution2(n, m):
    count = 0
    for i in range(n+1):
        for j in range((i+1)//2):         # Check the first half
            if n_Choose_k(i, j) > m:
                count += 2                # Double the number of valid checks
        if not i%2:                       # If i is odd, check iC(i+1)/2
            if n_Choose_k(i, i//2) > m:
                count += 1
    return count
'''
While this solution is very fast, we can still create a solution that is even faster. 
Although at first it seems counterintuitive, we actually end up taking far fewer
calculations by recreating Pascal's triangle, checking values as we go along. 
For each successive row, each value is simply the sum of the two values above it.   
'''
def solution3(n, m):
    n += 1
    pasc = []
    for i in range(n):
        pasc.append([0]*n)       # Initialize the Pascal's triangle array
    count = 0
    for i in range(n):
        pasc[i][0] = 1           # First value is always 1
        for j in range(1, i+1):
            pasc[i][j] = pasc[i-1][j-1] + pasc[i-1][j]   # Add two adjacent values above
            if pasc[i][j] > m:   # Check if greater than the limit
                count += 1
    return count
'''
This final solution scales up rather nicely, and requires much fewer calculations for larger 
values. 
'''
print('Number > 1,000,000:', solution3(100, 1000000))  # Number > 1,000,000: 4075



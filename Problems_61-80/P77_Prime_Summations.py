'''
Problem: What is the first value which can be written as the sum of primes
in over five thousand different ways?

In the same way as problem 76, problem 77 can be solved with the same algorithm
developed in problem 31. Now we will just need a list of all the primes less than
n, with the target amount set to n.
First we will bring back a quick and dirty algorithm for finding odd primes.
'''
def is_prime(n):
    for i in range(3, int(n**0.5+1), 2):
        if not n%i:
            return False
    return True
'''
In addition, we will need the coin summation algorithm from problem 31. 
'''
def optimal(primes, n):
    ways = [1] + [0]*(n)
    for i in range(len(primes)):
        for j in range(primes[i], n+1):
            ways[j]+=ways[j-primes[i]]
    return ways[n]
'''
And finally, all we need to do is finish off the solution with a bit of logic. Starting with
i=2 we will increment i by 1 each time, adding to the prime list if necessary, and checking
if the algorithm is greater than the specified limit.  
'''
def solution(n):
    i = 2
    primes = [2]                    # Initialize list of primes
    while optimal(primes, i) < n:   # Check if above limit
        i += 1
        if i%2 and is_prime(i):
            primes.append(i)        # Add to primes list if necessary
    return i

print('First with over 5000 ways:', solution(5000))  # First with over 5000 ways: 71

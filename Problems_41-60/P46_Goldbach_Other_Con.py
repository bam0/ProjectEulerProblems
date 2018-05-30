'''
Problem: What is the smallest odd composite that cannot be written
as the sum of a prime and twice a square?

For this problem we'll need a set of primes, and a list of squares.
First we pick a limit to work with, then get to work generating the
set of primes below that limit, as well as all the "double-squares"
below it. Then all we need to do is iterate over odd composite numbers,
subtracting successive double-squares from them until we find one where every
difference is composite.
First we borrow the all-too-familiar prime sieve we have been using.
'''
def prime_sieve(n):
    L = [True]*n
    L[0] = L[1] = False
    for i, is_prime in enumerate(L):
        if is_prime:
            yield i
            for x in range(i*i, n, i):
                L[x] = False
'''
And that's all we need to dig in to the solution. 
'''
def solution(limit):
    primes = set(prime_sieve(limit))      # Create prime set
    x, sq = 1, []                         # Initialize double-square set
    while 2*x*x <= limit:
        sq.append(2*x*x)                  # Add the double-squares
        x+=1
    num = 9
    while num < limit:                    # Iterate over odd numbers
        i, k = 0, 1
        if num not in primes:             # If it's composite, start subtracting
            while sq[i] < num:            # double-squares
                if num-sq[i] in primes:   # If it's prime, move on
                    k = 0
                    break
                i+=1
            if k:                         # Otherwise, the number is found
                return num
        num += 2

print('Disproof:', solution(10000))   # Disproof: 5777


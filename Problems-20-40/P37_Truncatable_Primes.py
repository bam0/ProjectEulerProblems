'''
Problem: Find the sum of the only eleven primes that are both
truncatable from left to right and right to left.
(e.g. 3797 -> 797 -> 97 -> 7 & 379 -> 37 -> 3)

As we don't immediately have a reasonable guess as to what we should make
our upper bound, let's go with 1 million for good measure.
First we borrow our handy prime sieve:
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
Now we generate a set of primes below a million. 
'''
big_set = set(prime_sieve(1000000))
'''
So now is the part of the problem where we have to do something
we haven't already done before. Here we will simultaneously truncate
the prime from the left and right, checking both for primality. 
'''
def is_truncatable(p):
    k, p1 = len(str(p))-1, p           # Get the exponent and a copy of p
    for i in range(k):
        p1 -= (p1//10**(k-i))*10**(k-i)          # Truncate to the right
        p//=10                                   # Truncate to the left
        if p not in big_set or p1 not in big_set:
            return False
    return True
'''
Now we just have to implement the above algorithm and check each
prime below 1 million. 
'''
def solution():
    truncs = set()                         # Initialize set of primes
    for p in big_set:
        if p in (2,3,5,7):                 # Don't add 2,3,5, or 7
            continue
        if is_truncatable(p):              # Check for the property
            truncs.add(p)
    print('Length:', len(truncs), truncs)
    return sum(truncs)
'''
Luckily we get all 11 without going above a million. 
'''
# Length: 11 {3137, 37, 739397, 73, 797, 53, 373, 23, 3797, 313, 317}
print('Sum of Truncatables:', solution())  # Sum of Truncatables: 748317
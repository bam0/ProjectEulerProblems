'''
Problem: How many circular primes are there below one million?
(E.g. 197 -> 197, 971, 719)

We know by now how to generate a set of primes below one million quickly
using a sieve. So really all we need to do here is figure out how to rotate
the digits of a prime and check if they are in the prime set. There's not much
more to it than that.
'''
def prime_sieve(n):
    L = [True] * n                         # Initialize the array of booleans
    L[0] = L[1] = False
    for (i, is_prime) in enumerate(L):
        if is_prime:
            yield i
            for x in range(i*i, n, i):     # Set the non-primes to False
                L[x] = False
'''
To rotate the digits quickly, we'll first find the number of digits, and take away
one to get the power of ten we need. Then we'll generate the next number by taking
the last digit, multiplying it by the power of ten, and adding it to the truncated
number. All we do after is check if it's in our set.
'''
prime_list = set(prime_sieve(1000000))
def check_circ(p):
    k = len(str(p))
    pow = 10**(k-1)                          # Find the power of ten we need
    for i in range(k-1):
        p = (p-p%10)//10 + (p%10)*pow        # Rotate the digits
        if p not in prime_list:              # Check if it's prime
            return False
    return True
'''
Now all we need to do is check every prime in our list.
'''
def solution():
    circs = set()              # Initialize the set of circular primes
    for p in prime_list:
        if check_circ(p):      # Check if it's in the set
            circs.add(p)
    return len(circs)          # Return the total number

print('Circular primes:', solution())   # Circular primes: 55


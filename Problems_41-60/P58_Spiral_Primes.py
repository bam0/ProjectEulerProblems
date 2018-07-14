'''
Problem: If the natural numbers are spiralled outward counterclockwise,
what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?

Given our previous knowledge of how to derive the numbers that lie on the diagonal
from problem 28, finding the answer becomes more about fast prime detection than
anything else. There are many, many ways of determining primality, but here we will
only use a couple of ways we already know. Of course there are much quicker methods
such as the Miller-Rabin test, and built-in functions from numpy, but we will not touch
on those for now.
First we'll use a very simple prime-checker that determines the primality of odd numbers
greater than 3.
'''
def is_prime(n):
    for i in range(3, int(n**0.5+1), 2):
        if not n%i:
            return False
    return True
'''
Starting with 1, we calculate the odd squares, then plug them into the formula we found in
problem 28 to generate the four numbers on the diagonal of each interior square. Then all we
need to do is check the primality of each of those numbers, and increment the number of primes
and the total count of all numbers on the diagonals. Since all the numbers on the diagonals 
must be odd, we are able to slim the typical brute-force prime-checking algorithm down to the
one above. Then after each iteration, we check and see if the ratio falls below the given value.  
'''
def solution1(r):
    primes, total = 0, 1             # Initialize number of primes & total along diagonal
    i = 1
    while True:
        sq = (2*i+1)**2              # Calculate odd square
        for _ in range(3):
            sq -= 2*i
            primes += is_prime(sq)   # Check if prime
        total += 4                   # Increment total
        if primes/total < r:         # Check if below given ratio
            return 2*i+1
        i += 1
'''
And for the second solution, we keep almost everything the same, except we change
the method used for checking primality. Here we borrow the dynamic primality check, 
which only checks the primes in a pre-made list until the root of the number is reached.
Everything should look pretty familiar still.
'''
def sieve(n):
    L = [True]*n
    L[0] = L[1] = False
    for i, prime in enumerate(L):
        if prime:
            yield i
            for x in range(i*i, n, i):
                L[x] = False

def dynamic_check(n, lst):
    root = n**0.5
    for p in lst:
        if p > root:
            return True
        if not n%p:
            return False
    return True
'''
The square root of a billion is used here as a benchmark for the dynamic primality checking
function above. 
'''
def solution2(r):
    p_lst = list(sieve(int(1000000000**0.5)))  # Initialize sufficiently large prime list
    primes, total = 0, 1
    i = 1
    while True:
        sq = (2*i+1)**2
        for _ in range(3):
            sq -= 2*i
            primes += dynamic_check(sq, p_lst)
        total += 4
        if primes/total < r:
            return 2*i+1
        i += 1
'''
This method gives a modest speed boost of about 2x, but relies on an estimate of the size
of the primes we need to check. Because the numbers get large very quickly, neither method
is very fast, and can easily be improved by more complex primality checking functions like
those mentioned in the preface. 
'''
print('Spiral side length:', solution2(0.1))  # Spiral side length: 26241

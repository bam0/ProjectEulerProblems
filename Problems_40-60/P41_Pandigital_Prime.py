'''
Problem: What is the largest n-digit pandigital prime that exists?

One way of going about the solution to this problem is to generate a
huge list of primes and check whether or not each one is pandigital.
This can be done with the use of a prime sieve and a simple check
that the digits are each of the numbers 1 - 9.
'''
def prime_sieve(n):
    L = [True]*n
    L[0] = L[1] = False
    for i, is_prime in enumerate(L):
        if is_prime:
            yield i
            for x in range(i*i, n, i):
                L[x] = False

def solution1(n):
    mx = 2143                                # 2143 is given
    digs = [str(i) for i in range(1, n+1)]   # Create list of digits
    primes = prime_sieve(10**n)
    for p in primes:
        if sorted(str(p)) == digs:           # Check if pandigital
            if p > mx:
                mx = p
    return mx
'''
After n=7, or up to 10,000,000, things get very slow with this algorithm.
Even though it still gives us the right answer, we can't be sure
there aren't more pandigital primes above 10^7. So how do we check these?
We could go the other direction - instead of checking each prime, we check 
each permutation of the digits 1-n by converting it into an integer, then 
checking for primality. This should give us a definitive answer. 
First we create a little prime checker:
'''
small_sieve = list(prime_sieve(31500))  # List up to ~sqrt(987654321)
def dynamic_check(n):
    root = n**0.5
    for i in small_sieve:
        if n%i==0:            # Check for primality
            return False
        if i > root:          # > root, so end the loop
            break
    return True
'''
Now we write a short program to convert a permutation into an integer:
'''
def get_int(perm):
    k = len(perm)
    return sum(perm[i]*10**(k-i-1) for i in range(k))
'''
And verify all the permutations of a given length: 
'''
from itertools import permutations
def verify_perms(n):
    mx = 0
    perms = permutations([i for i in range(1, n+1)])
    for perm in perms:
        num = get_int(perm)
        if num%2==0 or num%3==0:               # Get rid of junk
            continue
        if dynamic_check(num) and num > mx:    # Check for primality & max
            mx = num
    return mx
'''
Lastly, we run the program for each length 4 to 9.
'''
def solution2():
    return max(verify_perms(i) for i in range(4, 10))
'''
With the second solution, we are able to generate a definitive
answer in less time than it took to check up to 7-digit primes. 
'''
print('Max pandigital prime:', solution2()) # Max pandigital prime: 7652413

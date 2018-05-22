'''
Problem: Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive values of n,
starting with n=0. (n^2 + an + b where |a|<1000, |b|<=1000)

Trying all possible values of a and b, along with calculating if each
successive value is prime/not-prime would probably take quite a long time.
For this problem, we'll only need a couple of observations to help us speed our
search up.
1. b must be prime. For n=0, we are left with just b, therefore b is prime.
2. a must be odd.   When n is odd, we would be left with n^2 + even + b, and since
n^2 and b would be odd, the total sum would be even and thus not prime.
These facts alone surprisingly cut down a lot of searching.
We will be taking advantage of sets, and our nifty prime sieve to create the solution.
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
We create one big set of primes for checking against the quadratic equation, and
another small set of primes for initializing b.
'''
big_set = set(prime_sieve(100000))
small_set = set(prime_sieve(1000))
'''
Here we are simply plugging the values into the quadratic equation and checking 
if the result is prime.
'''
def num_primes(a,b):
    n = 0
    while(n*n+a*n+b in big_set):   # Check if the value is in the big prime set
        n+=1
    return n
'''
Finally, we iterate over all the values that we are left with. 
'''
def solution():
    mx = 0
    mx_ab = (0,0)                         # Initialize tuple of a and b
    for b in small_set:
        for a in range(1, 1000, 2):
            n1 = num_primes(a, b)         # Check a and b
            if n1 > mx:
                mx, mx_ab = n1, (a, b)
            n2 = num_primes(-a, b)        # Check -a and b
            if n2 > mx:
                mx, mx_ab = n2, (-a, b)
    print('{} * {} = {}'.format(*mx_ab, mx_ab[0]*mx_ab[1]))
    print('Max length:', mx)

solution()
#  -61 * 971 = -59231
#  Max length: 71

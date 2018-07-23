'''
Problem: How many elements would be contained in the set of reduced
proper fractions for d ≤ 1,000,000?

For any given d, there are φ(d) reduced proper fractions with denominator d, since we
are looking for all numerators relatively prime to d. In essence, this problem is asking
us to find the sum of φ(d) for 2<=d<=1mil. Considering we have already established a
formula for φ(d) in problems 69-70, we can borrow it here to generate a solution.
First comes the prime sieve.
'''
def sieve(n):
    L = [True]*n
    L[0] = L[1] = False
    for (i, is_prime) in enumerate(L):
        if is_prime:
            yield i
            for x in range(i*i, n, i):
                L[x] = False
'''
Then the formula for generating the factors of n. 
'''
def get_factors(n, primes):
    facs = []                   # Initialize list of factors
    root = n**0.5
    for p in primes:
        if p > root:            # If current p is greater than the root, we are done
            facs.append(n)
            return facs
        if not n%p:             # If p|n, add to factors
            facs.append(p)
            while not n%p:
                n//=p           # Now keep dividing n by p
            if n==1:            # If n=1, we are done
                return facs
    return [n]                  # If the end of the list is reached, n is prime
'''
And the totient calculator. 
'''
def totient(n, primes):
    facs = get_factors(n, primes)
    for fac in facs:
        n//=fac                 # Divide by each prime
        n*=(fac-1)              # Multiply by each prime-1
    return n
'''
The only thing else we need to write is a loop to sum over all the values of φ(d). 
'''
def solution1(n):
    tot = 0
    primes = list(sieve(int(n**0.5)+100))
    for i in range(2, n+1):
        tot+=totient(i, primes)
    return tot
'''
Although this solution is very straightforward and easy to implement from what we have
already established earlier, it is highly inefficient. We'll need to think of something
more clever to increase the speed. 
It turns out that there is an even easier way to find the answer to this problem, as long as
we have access to the primes below 1mil. We start by initializing a list of all the numbers
from 0 to 1mil, and generating a sieve of the primes below 1mil. Every time we come across
a prime p, we multiply all multiples of the prime in the list by (p-1)/p. Once we reach the
end of the sieve, what we are left with is a list of all the totients for each value of d.
All that remains is to sum the list (and take off 1).   
'''
def solution2(n):
    nums = [i for i in range(n+1)]   # Initialize totient list
    primes = sieve(n)                # Generate prime sieve
    for p in primes:
        for j in range(p, n+1, p):   # Multiply each multiple by (p-1)/p
            nums[j]//=p
            nums[j]*=(p-1)
    return sum(nums)-1               # Result is the sum of the list-1
'''
This gives us a solution over 10x faster than the previous one. However, it is still not nearly 
the fastest. See the overview for problem 73 on Project Euler for an optimized solution, as
it is much more comprehensive than I would be able to get into here. 
'''
print('Num. of elements in the set:', solution2(1000000)) # Num. of elements in the set: 303963552391



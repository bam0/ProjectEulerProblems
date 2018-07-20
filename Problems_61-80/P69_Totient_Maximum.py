'''
Problem: Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum
(where φ(n) denotes the totient function).

The seemingly most straightforward way of figuring out this problem would be to
find a formula for φ(n), and then find n/φ(n) for each number from 2-1,000,000,
returning the maximal value.
So how is φ(n) calculated? The formula is actually not quite so complicated. Since n
can be written as the product of primes p_1,...,p_k to a power, it is possible to
represent φ(n) as n*(p_1-1)...(p_k-1)/p_1...p_k. Thus if we can find each of the prime
factors of n, we can easily derive φ(n).
First we'll bring back our trusted prime sieve.
'''
def prime_sieve(n):
    L = [True]*n
    L[0] = L[1] = False
    for (i, is_prime) in enumerate(L):
        if is_prime:
            yield i
            for x in range(i*i, n, i):
                L[x] = False
'''
And now we'll modify one of the functions used previously for factoring a number, in order
to only give the distinct prime factors of n. 
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
One we have the factors of n, the totient is straightforward to calculate. 
'''
def totient(n, primes):
    facs = get_factors(n, primes)
    for fac in facs:
        n//=fac                 # Divide by each prime
        n*=(fac-1)              # Multiply by each prime-1
    return n
'''
The rest is simply calculating n/φ(n) for all number from 2 to one million.
We create another set of primes up to a million in order to make the algorithm
slightly quicker. 
'''
def solution1(n):
    primes = list(prime_sieve(1000))
    big_set = set(prime_sieve(1000000))
    mx, mx_num = 1, 1                     # Initialize max n/φ(n) and max n
    for m in range(2, n+1):
        if m in big_set:                  # If prime, keep checking
            continue
        cur = m/totient(m, primes)        # Calculate n/φ(n)
        if cur > mx:
            mx, mx_num = cur, m
    return mx_num                         # Return the maximal n
'''
The main drawback to this algorithm is that it is very slow. It takes over 20 seconds to
calculate a solution. So how can things be sped up? By using a little logic, the problem
becomes trivial, and can even be done by hand. Since φ(n) involves n in its formula, we can
cross n out to get a formula for n/φ(n) independent of n, only involving a set of distinct 
prime factors: p_1...p_k/(p_1-1)...(p_k-1). Adding a prime factor will increase the value of
n/φ(n), and adding smaller prime factors will increase the value more than larger primes. 
Therefore, the optimal solution will be the product of the most consecutive primes starting
at 2. 
While it is not difficult to find the first dozen or so primes by hand and multiply them,
we will still code this solution out. We start with a simple brute-force prime checker.  
'''
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True
'''
Now we just keep multiplying primes until we get something over 1 million, in which case
the previous number becomes the solution we are looking for. 
'''
def solution2(n):
    i = mx = 1
    while mx < n:
        i += 1
        if is_prime(i):
            mx*=i
    return mx//i
'''
Using this fact makes the solution come up in no time at all. 
'''
print('Value of n:', solution2(1000000))  # Value of n: 510510

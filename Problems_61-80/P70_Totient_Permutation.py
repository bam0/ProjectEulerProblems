'''
Problem: Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation
of n and the ratio n/φ(n) produces a minimum.

Considering how long it took to find an answer by brute force in the previous problem,
multiplying the number of cases by 10 will take exponentially longer. In that case we
will skip writing a brute force solution. Instead, we need to think about this a bit more
cleverly. The first thing to note is that the numbers with the smallest value of n/φ(n)
are large primes. However, φ(n) for a prime number is just n-1, which could not possibly
be a permutation of n. The next possible option would be squares of a prime, as the value of
n/φ(n) would be the same as the prime itself.
First we will grab our prime sieve again.
'''
def sieve(n):
   L = [True]*n
   L[0] = L[1] = False
   for i, is_prime in enumerate(L):
       if is_prime:
           yield i
           for x in range(i*i, n, i):
               L[x]=False
'''
Next we write a short helper function that checks if two numbers are permutations of 
one another.  
'''
def is_perm(a, b):
   return sorted(str(a)) == sorted(str(b))
'''
Next we will check all the primes up to sqrt(10^7), printing out any that may satisfy the
requirements of the problem. 
'''
def check_squares():
   sv = sieve(int(10000000**0.5)+1)
   primes = list(sv)[::-1]
   for p in primes:
       if is_perm(p*p, p*(p-1)):
           print(p, p*p)
'''
As it turns out, none of them actually do satisfy the requirements, so we are left looking
for another possibility. The next option would be the product of two large primes p & q. 
This gives a lot more possible options that could satisfy the conditions. 
First we'll need a helper function to give us n/φ(n) when n is a product of primes p & q. 
'''
def n_over_totient(p, q):
   return (p*q)/((p-1)*(q-1))
'''
In order to find the solution, instead of checking the product of every combination of
two primes, we will narrow the search to only combinations of primes above and below
sqrt(10^7). How it works is first the index of the prime just below sqrt(10^7) is found, 
and this becomes the starting point for the smaller prime. Then, as the index for the 
smaller prime goes down, another index increments the larger prime, until the product
of the two primes is above 10^7. Each time n is a permutation of φ(n), the value 
of n/φ(n) is calculated and compared until the resulting minimum is found.   
'''
def solution(n):
   sv = sieve(int(n**0.5)*2)          # Create prime sieve, padded with extra primes
   primes = list(sv)
   idx = primes.index(3137)           # Find index of prime just below sqrt(10^7)
   mx, lgt = (2,2,4), len(primes)     # Initialize max(p, q, p*q) and length of prime list
   for i in range(idx, 0, -1):
       j = idx+1                      # Start from the middle and work upward
       p, q = primes[i], primes[j]
       while p*q < n:
           if is_perm(p*q, (p-1)*(q-1)):
               if n_over_totient(p, q) < n_over_totient(mx[0], mx[1]):
                   mx = (p, q, p*q)
           j += 1
           if j > lgt-1:              # If we reach the end of the list, stop
               break
           p, q = primes[i], primes[j]
   return mx[2]
'''
Sure enough, using this method we are able to find many values of n which are also
permutations of φ(n), but only one gives the minimal value of n/φ(n). 
'''
print('Value with minimal n/φ(n):', solution(10000000)) # Value with minimal n/φ(n): 8319823



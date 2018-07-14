'''
Problem: Find the lowest sum for a set of five primes for which any two
primes concatenate to produce another prime.

This is one of the problems that has given me the most trouble, both when I originally
solved it and when I went back to make this guide. One of the primary issues is that there
are a large number of primes to run through, and checking for primality can be taxing without
the proper function. The main strategy employed here is to work through the primes going
upward from the beginning, each time creating a list of all the possible numbers than can
concatenate with it to produce two more primes. And for each of those possibilities, we check
if they will further concatenate to produce primes with the other numbers in the list greater
than them. This process is repeated until we reach 5 primes, or the list of remaining
possibilities is empty.
Since checking for primality by normal means, or by creating a large set would take too much
time, we employ the is_prime function from the publicly available pyprimes library.
'''
import pyprimes as pyp
'''
However we will still need to generate a prime sieve to run through our list. 
'''
def sieve(n):
    L = [True]*n
    L[0] = L[1] = False
    for i, prime in enumerate(L):
        if prime:
            yield i
            for x in range(i*i, n, i):
                L[x] = False
'''
The following helper function checks to see if two primes will concatenate to 
produce two more primes. 
'''
def is_pair(a, b):
    s1, s2 = str(a), str(b)
    if pyp.is_prime(int(s1+s2)) and \
        pyp.is_prime((int(s2+s1))):
        return True
    return False
'''
Now we get into the meat of the solution. The function takes in a length n, and a limit for
the number of primes to check. Within that function, we have another function called mn_set
which recursively goes through all the possible primes that will concatenate with one another
in order to find the minimum sum of length n. For each iteration, the first element of the 
list rest is added to the list pairs, and the list rest is subsequently reduced to only those 
primes which concatenate with that element. Once the list rest is empty, we check if the
length of pairs is n, otherwise return 0. 
'''
def solution(n, limit):
    p_lst = list(sieve(limit))                   # Generate prime sieve
    def mn_set(pairs, rest):
        if not rest:                             # Check if rest is empty
            if len(pairs) == n:                  # If length = n, return the sum
                return sum(pairs)
            return 0                             # Else, return 0
        else:
            r = len(rest)
            mn = 1000000                         # Create an upper bound for the sum
            k = 50 if r > 50 else r              # Limit num of searches to increase speed
            for i in range(k):
                cur, temp = rest[i], []          # Set cur equal to first element of rest
                for j in range(i+1, r):          # Check each subsequent element of rest
                    if is_pair(cur, rest[j]):
                        temp.append(rest[j])     # If valid, add to new list
                m = mn_set(pairs + [cur], temp)  # Check the next iteration
                if 0 < m < mn:                   # If between 0 and the minimum, set new mn
                    mn = m
            return mn
    return mn_set([], p_lst)                     # Search through the entire prime list
'''
Even with some tweaking of limits, the algorithm still takes a few seconds to run. 
There are surely faster algorithms to tackle this problem, but this was the solution that
I managed to come up with. 
'''
print('Smallest sum:', solution(5, 10000))  # Smallest sum: 26033


'''
Problem: Find the first four consecutive integers to have four
distinct prime factors each. What is the first of these numbers?

We will be showcasing a couple different approaches to this problem again.
The first is the more straightforward, which is just using an algorithm to calculate the
number of distinct prime factors for every number until we get a streak of four.
It goes without saying we need to borrow our prime sieve yet again.
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
We now generate a list of primes to handle all cases up to 1 million.
'''
primes = list(prime_sieve(1000))
'''
And now all we have to do is modify the algorithm from problem 12 for the 
number of divisors of a number. Instead of keeping a product, all we need
to do is keep track of how many distinct divisors are dividing into the 
number. 
'''
def num_distinct(n):
    count = 0                         # Initialize count to 0
    if n==1:
        return count+1
    for i in range(len(primes)):
        p = primes[i]
        if p**2 > n:                  # If p^2 > n, we know n must be prime!
            return count+1
        k = 0                         # Checker for if p divides n
        while not n%p:
            k = 1
            n//=p                     # Keep dividing out by the prime
        count += k
        if n==1:                      # n=1, so nothing more to see here
            break
    return count
'''
Now we're pretty much done. All we have to do is keep a while loop that counts up from
1 until we get a string of four straight numbers with 4 distinct divisors. 
'''
def solution1(n):
    i, count = 1, 0
    while count < n:
        if num_distinct(i) == n:
            count+=1
        else:
            count = 0
        i+=1
    return i-n                    # Return the first number
'''
Despite being relatively brute force, this algorithm still gets the job done 
in less than 2 seconds. But we can do even better by using - you guessed it - dynamic
programming. How this next algorithm works is very similar, in fact, to the sieve of
Eratosthenes. Instead of setting the values of multiples of a prime to False, we just
add one to them, since we have just added a distinct divisor to them. This way we
essentially construct all the multiples under the limit n, adding one whenever a new
divisor is added. 
'''
def solution2(n):
    nums = [0]*n                        # Initialize the list of numbers
    for i in range(2, n):               # Start with the first prime - 2
        if not nums[i]:                 # If we get a prime, add 1 to the multiples
            for j in range(2*i, n, i):
                nums[j] += 1
    count = idx = 0                     # Now find a string of four 4's
    while count < 4:
        if nums[idx] == 4:
            count += 1
        else:
            count = 0
        idx += 1
    return idx - 4                      # Return the first number
'''
This algorithm is leaps and bounds faster than the first one, mainly because it takes
away a lot of repeated calculations.
'''
print('First of four:', solution2(150000))  # First of four: 134043


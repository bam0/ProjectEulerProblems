'''
Problem: What is the 10,001st prime number?

There are countless approaches to this problem that could provide the correct
solution, but I will only provide a few here. Each will utilize the functions we've
already seen previously in Problem 3.

First is the more brute-force way. We just keep checking numbers until we reach a count
of 10001 by using our prime-checker.
'''
import math
def prime_checker(n):
    for i in range(3, int(n**0.5+1), 2):  # Increment up to sqrt(n) by 2
        if n%i==0:
            return False
    return True

def solution1(n):
    count, num = 1, 1                     # Start the count at 1 since 2 is prime
    while(count!=n):
        num+=2
        if prime_checker(num):
            count+=1
    return num
'''
Next we will take advantage of the Sieve of Eratosthenes. The only problem is that
this method is much better for finding primes below a certain limit, as opposed
to finding the nth prime. 
'''
def primes_sieve(n):
    a = [True] * n                         # Initialize the array of booleans
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for x in range(i*i, n, i):     # Set the non-primes to False
                a[x] = False
'''
You will see now that we are setting the limit for the prime sieve to be a
seemingly arbitrary expression. What we're actually doing is using the approximation
for the number of primes - pi(x) ~ x/ln(x) - with a bit of padding, since the formula
is less precise for smaller numbers.
'''
def solution2(n):
    Sieve = primes_sieve(int(n*math.log(n)*1.25))    # Initialize sieve with pi(n) approx.
    cur, count = 1, 1
    for prime in Sieve:
        cur = prime
        if count == n:
            return cur
        count+=1
'''
Finally, let's be a little bit more clever about this. When we were creating
the first solution, when checking for each prime, we had to go through all the odd
numbers again and again. This is pretty wasteful. So what can we do? How about, instead
of checking all the odd numbers, let's just keep a running list of all the primes 
we've already found. When a new prime is found, append it to the list. We also only need
to check all the primes less than the square root of the number.  
This is known as dynamic programming, where we store previous solutions to help solve
those that follow. 
'''
def dynamic_prime_check(lst, num):
    root = num**0.5                    # Get the square root
    for prime in lst:
        if prime>root:                 # No more checks needed
            break
        if not num%prime:
            return False
    return True

def solution3(n):
    primes, count, cur = [2], 1, 3               # Initialize the primes list
    while(count!=n):
        if dynamic_prime_check(primes, cur):     # Dynamically check if cur is prime
            primes.append(cur)
            count+=1
        cur+=2                                   # Check each odd number
    return primes[-1]                            # Return the last one
'''
It turns out that the final solution is over 7x faster than the previous two!
It goes to show that dynamic programming can be a very useful tool.
'''
print("10,001st prime:", solution3(10001))   # 10,001st prime: 104743





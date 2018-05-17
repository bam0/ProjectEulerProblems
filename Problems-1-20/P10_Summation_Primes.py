'''
Problem: Find the sum of all the primes below two million.

This is familiar territory by now. Let's use the three prime generating methods we've
already used to help us with this problem. Then we'll see which is the fastest.

First up is the brute-force approach:
'''
def prime_checker(n):
    for i in range(3, int(n**0.5+1), 2):  # Increment up to sqrt(n) by 2
        if n%i==0:
            return False
    return True

def solution1(n):
    total = 2
    for i in range(3, n, 2):
        if prime_checker(i):
            total+=i
    return total
'''
Now for the Sieve of Eratosthenes:
'''
def primes_sieve(n):
    a = [True] * n                         # Initialize the array of booleans
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for x in range(i*i, n, i):     # Set the non-primes to False
                a[x] = False

def solution2(n):
    total, Sieve = 0, primes_sieve(n)
    for i in Sieve:
        total+=i
    return total
'''
Finally, the updating prime list method:
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
    primes, total = [2], 2
    for i in range(3, 2000000, 2):
        if dynamic_prime_check(primes, i):
            total+=i
            primes.append(i)
    return total
'''
At the end of the day, the Sieve of Eratosthenes reigns supreme. 
It performed over 10x as fast as the dynamic method, and over 20x as fast
as the brute force method.
'''
print('Sum of primes below 2mil:', solution2(2000000))
# Sum of primes below 2mil: 142913828922


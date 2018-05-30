'''
Problem: Find the sum of all the positive integers which cannot be
written as the sum of two abundant numbers.

Using the algorithms we already created in problem 21, this problem won't present
us with too much of a challenge. First we'll generate a list of primes with our
prime sieve, then calculate the sum of divisors for each number up to 28123
(which has been proven to be the last number not expressible as the sum of two
abundant numbers).
'''
def prime_sieve(n):
    L = [True] * n                         # Initialize the array of booleans
    L[0] = L[1] = False
    for (i, is_prime) in enumerate(L):
        if is_prime:
            yield i
            for x in range(i*i, n, i):     # Set the non-primes to False
                L[x] = False

primes = list(prime_sieve(200))        # sqrt(30000) ~ 170, plus some padding

def sum_div(n):
    prod, n_copy = 1, n                # Initialize the product and a copy of n
    if n==1:
        return 1
    for p in primes:
        if n < p*p:                    # Now we know n is prime, so add this to our product
            prod*=(n*n-1)//(n-1)
            break
        exp = 1                        # Initialize the exponent
        while not n%p:
            n//=p
            exp+=1
        prod*=int((p**exp-1))//(p-1)   # Plug p and exp into our formula
        if n==1:                       # When n is 1, we have no more primes to check
            break
    return prod-n_copy                 # Subtract off the copy of n
'''
One method we could use is to create a set of all the numbers that CAN be 
written as the sum of two abundant numbers. Then we just have to subtract that from the
sum of all the numbers from 1 to 28123. 
'''
def solution1():
    abund, non = [], set()               # Initialize the abundant and non-abundant list/set
    for i in range(1, 28124):
        if sum_div(i) > i:               # Check abundancy
            abund.append(i)
            for a in abund:
                sm = a+i
                if sm < 28124:           # Check if sum is in range
                    non.add(sm)          # Add it to our set
                else:
                    break
    return ((28123*28124)//2)-sum(non)   # Subtract from the total sum
'''
However a slightly faster solution is to generate a list of all the numbers from 1 to 28123
first. Then whenever a number can be written as an abundant sum, we just set its value to
zero. This is similar to the method used in the prime sieve. 
'''
def solution2():
    nums = list(range(1, 28124))       # Initialize list of numbers
    abund = []
    for i in range(1, len(nums)+1):
        if sum_div(i) > i:
            abund.append(i)
            for a in abund:
                sm = a+i
                if sm < 28124:
                    nums[sm-1] = 0     # Set value equal to 0
                else:
                    break
    return sum(nums)                   # Take the sum of the remaining numbers
'''
The result is still not very fast, taking ~2 seconds to complete. But this may be
more of a limitation of python, rather than the algorithm itself. 
'''
print('Non-abundant sum:', solution2())   # Non-abundant sum: 4179871

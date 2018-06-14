'''
Problem: Find the smallest prime which, by replacing part of
the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.

One of the first things we should try to do in order to solve this
problem is narrow down how many digits we need to replace. If we
replace 1 or 2 digits, we are guaranteed at least three numbers will
not be prime, since they would have to be divisible by 3. We know this
because if a number is divisible by 3, the sum of the digits is also
divisible by 3. Thus we should be focusing on replacing 3 digits.
And we also know that we cannot replace the final digit, because trivially we
would get 5 even numbers.
Combining these two facts will lead us to a more efficient solution.
Before getting started with the rest, let's bring out our prime sieve.
'''
def sieve(n):
    L = [True]*n
    L[0] = L[1] = False
    for p, prime in enumerate(L):
        if prime:
            yield p
            for i in range(p*p, n, p):
                L[i] = False
'''
First we'll need a helper function which takes in a prime and lets 
us know if we have a triple of the same digit. In order to avoid
redundant calculations, we save the value of the digit for the triple
as well and return it.  
'''
def triple(p):
    s, D = str(p), {}              # Initialize dictionary of digits
    for l in s:                    # Mimic the Counter built-in
        if l in D:
            D[l] += 1
        else:
            D[l] = 1
    for key, val in D.items():
        if val==3 and key!=s[-1]:  # Check for triple w/ last digit not included
            return (True, key)
    return (False, None)
'''
Now we'll create another helper function which checks if a given prime produces
an 8+ prime family through substitution of the key digit. It will check for primality
using the big set, and keep track of those already checked in the small set. All we 
need to do is take advantage of the sub function in the regex library. As long as there
are not over 2 composite numbers, we know we have found an 8-prime family.   
'''
import re
def is_valid(prime, small_set, big_set, key):
    count, p_str = 0, str(prime)
    for i in range(10):
        p_int = int(re.sub(key, str(i), p_str))              # Substitute key with 0-9
        if p_int in big_set and len(str(p_int))==len(p_str): # Checks if number is prime
            small_set.add(p_int)                             # and same length as the
        else:                                                # original number
            count += 1
        if count > 2:       # If >2 composite, test is failed
            return False
    return True
'''
The final part is simple. All we have to do is create a large list of primes with 
the sieve and check each of them for the above property. 
'''
def solution1(limit):
    big_list = list(sieve(limit))
    big_set = set(big_list)
    p_set = set()
    for prime in big_list:
        trp = triple(prime)
        if trp[0]:
            if prime in p_set:
                continue
            if is_valid(prime, p_set, big_set, trp[1]):
                return prime
'''
Next we'll craft a solution very similar to the previous one, but
without the use of a prime sieve. 
First we'll need a simple prime-checker. 
'''
def is_prime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if not n%i:
            return False
    return True
'''
The next function is almost the same as is_valid, with the sets 
removed and is_prime implemented instead. 
'''
def is_good(prime, key):
    count, p_str = 0, str(prime)
    for i in range(10):
        p_int = int(re.sub(key, str(i), p_str))
        if is_prime(p_int) and len(str(p_int))==len(p_str):
            continue
        count += 1
        if count > 2:
            return False
    return True
'''
Finally we start with 4 digit numbers and work our way up.
'''
def solution2(limit):
    cur = 1001
    while cur < limit:
        if is_prime(cur):
            trp = triple(cur)
            if trp[0] and is_good(cur, trp[1]):
                return cur
        cur += 2
'''
Lastly, we make a slight optimization over the previous solution
by using a smaller prime sieve than solution 1 coupled with a 
dynamic primality check. 
'''
def dynamic_check(lst, num):
    root = num ** 0.5     # Get the square root
    for prime in lst:
        if prime > root:  # No more checks needed
            break
        if not num % prime:
            return False
    return True
'''
And finally we take advantage of the fact that all primes after 3
can be written as 6k+/-1 for integers k. Now we have made a hybrid of
the first two solutions, giving the most efficient solution of the three. 
'''
def solution3(limit):
    prime_list = list(sieve(int(limit**0.5)))
    cur = 1002
    while cur < limit:
        if dynamic_check(prime_list, cur-1):       # Check 6k-1
            trp = triple(cur-1)
            if trp[0] and is_good(cur-1, trp[1]):
                return cur-1
        if dynamic_check(prime_list, cur+1):       # Check 6k+1
            trp = triple(cur+1)
            if trp[0] and is_good(cur+1, trp[1]):
                return cur+1
        cur += 6

print('Smallest prime:', solution3(1000000))  # Smallest prime: 121313
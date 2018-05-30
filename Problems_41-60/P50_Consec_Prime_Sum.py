'''
Problem: Which prime, below one-million, can be written as the sum of
the most consecutive primes?

We now have yet another problem involving primes. Our prime sieve will never
seem to catch a break. Anyway, this problem presents us with an interesting
challenge. How do we calculate sums efficiently, and how do we check primality
efficiently?
Before we start trying to develop a solution, let's go ahead and get the prime
sieve out of the way.
'''
def prime_sieve(n):
    L = [True]*(n)
    L[0] = L[1] = False
    for i, is_prime in enumerate(L):
        if is_prime:
            yield i
            for x in range(i*i, n, i):
                L[x] = False
'''
So how will we go about this first? It seems like we should first generate a list of all 
the primes below the limit so that we can sum them, and then put them in a set so we
can efficiently check primality. After that, we sum the primes from the beginning until we
hit a total above the limit n. Once we have this, and the index where the final prime was
located, we "shift" the window of primes we are looking at from the maximal length downwards.
We can make this efficient by taking away the prime on the very left, and adding the
prime on the very right. This will increase the sum until we get to the limit again, 
then we keep trying this for smaller and smaller lengths.  
'''
def solution1(n):
    p_lst = list(prime_sieve(n))    # Initialize the prime list
    p_set = set(p_lst)              # And the set
    i, total = -1, 0                # Index and current total
    while total < n:
        i += 1
        total += p_lst[i]           # Keep adding primes until the limit is reached
    total -= p_lst[i]
    i -= 1
    if total in p_set:              # Check if total is prime
        return total
    for j in range(i, 0, -1):       # Otherwise check different lengths from i downward
        total -= p_lst[j]           # Take away the rightmost element
        temp = total
        k = 0                       # Index to increase by
        while temp < n:
            if temp in p_set:       # If we find a prime, we are done
                return temp
            temp -= p_lst[k]        # Take away the left
            temp += p_lst[j+k]      # Add the right
            k += 1
'''
This will get the job done in a reasonable amount of time, but almost all of that
time is spent generating the list of primes and the associated set. And this is despite
the fact that we will only need a tiny sliver of the primes generated to calculate the
maximal sums. 
So what can we do to speed things up? How about keeping a list of sums instead. And then we
can use another prime sieve to generate only primes up to sqrt(n) to save us a lot of time
and memory checking primality. If we keep a running list of sums, then the difference between
any two sums will be the same as the consecutive sum of the primes between those two sums.
Then we can just loop through the list of sums, find the differences, and return the one
that gives us the max length. 
This solution proves yet again how dynamic programming can help us significantly.
First we borrow a helper function from problem 7 to speed up primality checking.   
'''
def is_prime(L, n):
    root = n**0.5
    for p in L:
        if p > root:
            break
        if not n%p:
            return False
    return True
'''
And now we craft the solution. 
'''
def solution2(n):
    sums = [0]                                # Initialize prime sum list
    primes = list(prime_sieve(int(n**0.5)+1))
    for p in primes:                          # Go ahead and add primes to sum list
        sums.append(sums[-1]+p)
    next = primes[-1]+2                       # Now extend the list
    while sums[-1] + next < n:
        if is_prime(primes, next):            # Use dynamic prime checker
            sums.append(next + sums[-1])
        next += 2
    size = len(sums)
    mx_len = mx_num = 0                       # Needed to check we have the max length
    for i in range(size-1, 0, -1):            # i starts on the right side
        for j in range(i-1):                  # j starts on the left
            temp = sums[i] - sums[j]
            if is_prime(primes, temp):
                if i-j > mx_len:              # Create new max length
                    mx_len, mx_num = i-j, temp
                if mx_len > i:                # If it's not possible to go further, we're done
                    return mx_num
                break
'''
This solution is leaps and bounds better than the previous one, improving efficiency 
to O(sqrt(n)) instead of O(n).
'''
print('Most consecutive sum:', solution2(1000000)) # Most consecutive sum: 997651

'''
Problem: Find the sum of all 0 to 9 pandigital numbers with the property that
each group of 3 digits is divisible by 2, 3, 5, ... 17 starting from the 2nd digit.

This is one of those problems that is confusing at the onset. There seem to be
so many different possible ways of approaching the problem that it's hard to
settle down with anything. Clearly we are better off not computing all 3 million+
possible numbers and testing them for the divisibility property.
One thing we could do instead is to try and construct solutions instead of blindly
checking them. That would allow us to save a lot of time and memory.
So how would this be done? We could start from the beginning, but it would actually be
much faster to start from the end. First we look at all the multiples of 17, then append
a digit to the front if it's a multiple of 13, and keep going until we satisfy all the
divisibility properties. Each time we make sure to only add digits if they are distinct.
Let's get started.
First we initialize our list of primes, sans 17. You'll notice we add 1 at the end.
We add this here to make sure the last remaining digit is added to each pandigital.
'''
primes = [13, 11, 7, 5, 3, 2, 1]
'''
Now we write a helper function to turn each multiple of 17 into a list of digits, to
make computations simpler moving forward. 
'''
def get_digits(n):
    L = []
    while n > 0:
        L.insert(0, n%10)       # Insert the next digit to the front.
        n//=10                  # Get rid of the last digit
    if len(L) < 3:
        L.insert(0,0)           # Add 0 if less than 100
    return L
'''
Now we initialize the list of pandigital numbers with the multiples of 17
below 1000. 
'''
pand = []
for i in range(17, 1000, 17):
    digs = get_digits(i)
    if len(digs) == len(set(digs)):
            pand.append(digs)
'''
The next helper function will come in handy at the end of the program, when we 
need to find the sum of all the lists of digits. We are just pulling it from 
problem 20.  
'''
def add(lst1, lst2):
    r, j = 0, -len(lst2)-1           # r = remainder, j = beginning of lst2
    for i in range(-1, j, -1):       # Go backwards from the end -> start of lst2
        r, lst1[i] = divmod(r+lst2[i]+lst1[i], 10)     # Add the digits, get the remainder
    while r and j >= -len(lst1):     # If r>0 and we're not at start of lst1, keep going
        r, lst1[j] = divmod(r+lst1[j], 10)
        j-=1
    if r:
        lst1.insert(0, r)            # If we're at the beginning of lst1, insert the remainder
'''
Finally it's time for the meat of the algorithm. For each prime, we check if we can add 
a digit to the front of each number in the list that would make it so that the first three
digits are divisible by it. We make a new list of each of these possibilities and refresh
the previous one. 
'''
def solution():
    for p in primes:
        n_pand = []                             # Initialize new list
        for pan in pand:                        # Iterate over each value in prev list
            for i in range(10):
                if i not in pan \
                    and (i*100+pan[0]*10+pan[1])%p==0:  # Check if dictinct digits,
                    n_pand.append([i]+pan)              # and divisible by prime
        pand[:] = n_pand                        # Refresh the list
    sm = pand[0]
    for pan in pand[1:]:
        add(sm, pan)                            # Add the pandigitals together
    return ''.join(list(map(str, sm)))

print('Pandigital sum:', solution()) # Pandigital sum: 16695334890

'''
Problem: There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
having the same set of digits, but there is one other 4-digit sequence. What 12-digit number
do you form by concatenating the three terms in this sequence?

This is probably one of my favorite problems of the first 50. There are two primary ways of
going about this problem: 1) Find arithmetic sequences of primes first, then check for
their digits, and 2) Find permutations of primes first, then check if there is an arithmetic
sequence. We will start with the first approach.
First we'll need a prime sieve to generate all the 4-digit primes.
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
Now we utilize our prime sieve to create a list - and set - of all the primes from 1,000
to 10,000. 
'''
p_lst = list(filter(lambda x: x > 1000, prime_sieve(10000)))
p_set = set(p_lst)
'''
And now we're ready to create our first solution. We iterate over the primes in our list
in a pairwise fashion, calculating what the third term in the arithmetic progression would
be. Then we check the numbers for being permutations of one another, as well as the third 
number being prime. 
'''
def solution1():
    count, perms = 0, []                # Initialize our list of primes satisfying the property
    for i in range(len(p_lst) - 1):
        j = i+1
        third = 2*p_lst[j] - p_lst[i]   # Calculate the third term in the progression
        while third < 10000:
            if third in p_set:          # Check if it's prime and all three are permutations
                if sorted(str(p_lst[i])) == sorted(str(p_lst[j])) \
                        and sorted(str(p_lst[j])) == sorted(str(third)):
                    count+=1
                    perms.append((p_lst[i], p_lst[j], third))  # Gather the triplet
                    if count == 2:
                        return ''.join(map(str, perms[1]))
            j+=1
            third = 2*p_lst[j] - p_lst[i]    # Otherwise, keep checking
'''
This solution is perfectly valid, and runs rather quickly, but there's still one more
path we haven't gone down yet. We could first generate permutations of each prime and then
check if there are any arithmetic sequences contained within them. 
First we import permutations and create a helper function to convert them into integers.
'''
from itertools import permutations
def make_num(tup):
    return int(''.join(tup))
'''
So now we can set to work with the second solution. 
'''
def solution2():
    count, concat, = 0, set()               # Initialize set of solutions
    for prime in p_lst:
        perms = permutations(str(prime))    # Generate permutations of the prime
        perms = list(set((filter(lambda x: x>1000, map(make_num, perms)))))
        P = []
        for perm in perms:                  # Add those that are prime
            if perm in p_set:
                P.append(perm)
        if len(P) > 2:                      # Check for arithmetic progression
            for i in range(len(P)-2):
                for j in range(i+1, len(P)-1):
                    third = 2*P[j] - P[i]
                    if third in P:          # If so, add to the set
                        concat.add((P[i], P[j], third))
        if len(concat) > 1:
            for c in concat:
                if c[0] != 1487:            # Print out the correct solution
                    return ''.join(map(str, c))
'''
And it turns out that the second solution is the winner of the race, with over
10x the speed of the previous solution, even despite the fact both methods are pretty fast. 
'''
print('Prime sequence:', solution2())  # Prime sequence: 296962999629
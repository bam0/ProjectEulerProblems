'''
Problem: Find the pair of pentagonal numbers, Pj and Pk, for which their
sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

This may be one of the most difficult out of the first 50 problems. The main issue is that
the result is fairly large, and can take quite a long time even with moderately efficient
code. We'll be looking at a couple solutions here, one that I made and the next that I
reformulated from another Project Euler user.
The approach I used was to make a moderately large set of pentagonal numbers first, then
start taking pairwise sums of elements until I find one that is in the same set, or the sum
is too small to be in the set. Subsequently, the sum is added to each of its summands,
and if this result is in the set, the other summand must be the difference that we need.
This is somewhat convoluted, but it saves a bit of time.
'''
def solution1(size):
    pents = set(n*(3*n-1)//2 for n in range(1, size))  # Generate a set of pent numbers
    pent_lst = list(pents)                             # And a list
    for i in range(1, len(pent_lst)-1):
        j = i - 1
        sm = pent_lst[i] + pent_lst[j]                 # Find the sum
        while sm >= pent_lst[i+1]:                     # Go until the sum cannot be in the set
            if sm in pents:                            # Check if sum is in set
                if pent_lst[j] + sm in pents:
                    return pent_lst[i]                 # Return difference
                elif pent_lst[i] + sm in pents:
                    return pent_lst[j]
            j -= 1
            if j > -1:
                sm = pent_lst[i] + pent_lst[j]         # Make sure there is no index error
            else:
                break
    return 0
'''
This solution is decent, but we can do better. One approach is to forgo making a 
large set to start off with, but instead use a generator. We use dynamic programming
to keep a running set of pentagonal numbers, and when we find a difference that is also
a pentagonal number, we associate it as a value to its sum. That way, as soon as the 
corresponding sum shows up, we know we have a valid solution, and it must be the minimum.
'''
def pent_gen():             # Create a generator for pentagonal #'s
    n = 1
    while True:
        yield n*(3*n-1)//2
        n += 1

def solution2():
    pents, sums = set(), {}           # Initialize the pent set, and sums dictionary
    for p in pent_gen():
        if p in sums:                 # When we get a valid sum, we are done
            return sums[p]            # Return the difference
        for num in pents:
            if p-num in pents:        # Check if each difference is in the set
                sums[p+num] = p-num   # Associate the difference to its sum
        pents.add(p)
'''
This solution runs about 3-4 times faster than the previous one.
'''
print('Minimal difference:', solution2()) # Minimal difference: 5482660

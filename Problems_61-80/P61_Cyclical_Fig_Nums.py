'''
Problem: Find the sum of the only ordered set of six cyclic 4-digit numbers
for which each polygonal type: triangle, square, pentagonal, hexagonal,
heptagonal, and octagonal, is represented by a different number in the set.

This is a particularly fun problem with surprisingly only one solution. Despite the fact
that the problem statement gives formulae for finding each figurate number individually,
we can in fact write a single function for finding any figurate number with relative ease.
In the function below, the number i increments by v each time, while the number m increments
by i. v=1 corresponds to triangle numbers, v=2 with squares, and so on.
In order to speed up checking pairs of two digits later on, we create a dictionary where
each key is the first two digits of a figurate number, and each value is the list of all
pairs of digits that create a valid number with the key.
'''
def fig(v, n):
    i = m = 1
    r = 10**n                       # Limit search to 4 digit numbers
    D = {}                          # Initialize dictionary
    while m < r:
        fir, las = divmod(m, 100)   # Get the first and last pair of digits
        if fir > 9 and las > 9:
            if fir not in D:        # Create the key value pair
                D[fir] = [las]
            else:
                D[fir].append(las)  # Otherwise add more valid digits to the list
        i += v
        m += i
    return D
'''
Now we're ready to move on to the solution. What we will do is take in a permutation of 
each of the dictionaries corresponding to each figurate type (tri, square, etc.). Then we 
will try to find a cycle of digits that starts from the first dictionary and wraps back around.
The list chain will keep track of which digits we have checked. The algorithm will check if 
the last pair of digits in chain has a corresponding pair in the next dictionary in the list.
If we get a complete chain, we set the global list answer equal to chain. 
'''
answer = []                                # Initialize global list answer
def check_perm(idx, lst, chain):
    global answer
    if idx == 5:                           # If at end of list, check if valid chain
        if chain[0] in lst[5][chain[5]]:
            answer = chain
    elif idx == 0:                         # If at beginning of list, check through entire dct
        dct = lst[0]
        for key, val_lst in dct.items():
            for val in val_lst:
                if val in lst[idx+1]:      # If in next dct, continue checking
                    check_perm(idx+1, lst, [key, val])
    else:
        dct = lst[idx]
        cur = chain[-1]                    # Otherwise check only the last number in chain
        for val in dct[cur]:
            if val in lst[idx+1]:
                check_perm(idx+1, lst, chain+[val])
'''
Finally, all that remains is to generate all of the necessary permutations and keep checking
them until we finally hit on a solution. Then we simply multiply the sum of the numbers in 
the list answer by 101 to get the sum we want.  
'''
import itertools as it
def solution():
    figs = list(fig(i, 4) for i in range(1, 7))   # Generate list of each figurate num dct
    perms = it.permutations(figs)                 # Get the 6! permutations
    for perm in perms:
        check_perm(0, perm, [])
        if answer:                                # If we get something valid, return it
            return 101*sum(answer)
'''
Surprisingly, the solution takes only a couple milliseconds to find.
'''
print('Cyclic sum:', solution())  # Cyclic sum: 28684

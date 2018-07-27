'''
Problem: Given that the three characters are always asked for in order,
analyze the file so as to determine the shortest possible secret passcode
of unknown length.

While a problem like this presents many possible ways to solve it, I will choose
to focus on two particular algorithms: one that fails, and one that works.
In fact, since the number of distinct login attempts is so small, this problem can easily be
solved using the second method with a pen and paper.
But first we'll need to read the file and form a set of distinct 3-digit login attempts.
'''
def gen_keys():
    with open('keylog', 'r') as keylog:
        line = keylog.readline().strip()
        keys = set()
        while line:
            keys.add(line)
            line = keylog.readline().strip()
        return keys
'''
The following is an attempt at the solution I came up with that happens to be close
to the solution, but not quite. It relies on a probabilistic approach, which places
greater weights on digits in the 1st position, and lower weights on digits in the 2nd and
3rd positions. Digits are then placed in order of score from left to right, highest to 
lowest.     
'''
def almost_solution():
    D = {}                                    # Create dictionary to store digits
    for key in gen_keys():
        for i in range(3):                    # Add 100, 10, 1 to digits in the
            num = key[i]                      # 1st, 2nd, and 3rd positions
            if num in D:
                D[num]+=(10**(2-i))
            else:
                D[num] = 10**(2-i)
    L = [(key,val) for key,val in D.items()]  # Now create a list of the digits and sort
    L.sort(key=lambda k: k[1], reverse=True)  # based on score
    print(L)
    code = ''
    for val in L:
        code += val[0]
    return code                               # Give result in string form
'''
Although this algorithm gives the wrong answer with the given sample, it may be a viable 
strategy given a large enough sample size. It's also fun to play around with different 
weights, seeing which one produces the closest answer.
With that out of the way, it's time to think of a more thorough way of producing an answer.  
The following algorithm works by taking in a string of digits as a guess, then for each pattern,
the digits are swapped such that the pattern is satisfied. When all patterns are satisfied, the
algorithm is over. For each pair of digits in the pattern, the positions of the digits within
the string are found and swapped if necessary. Lists are used here, since strings are immutable.   
'''
def combine(pat, s):
    for i in range(len(pat)-1):
        l = s.index(pat[i])               # Find the left digit position
        for j in range(i+1, len(pat)):
            r = s.index(pat[j])           # Find the right digit position
            if r < l:
                s[l], s[r] = s[r], s[l]   # Swap if necessary

def solution():
    r = []                                # Initialize digit list
    for key in gen_keys():
        for x in key:
            if x not in r:                # Add any digits not in the list
                r.append(x)
        combine(key, r)                   # Swap to fit the current pattern
    return ''.join(r)
'''
Now the algorithm produces a solution in less than a millisecond. 
'''
print('Shortest possible passcode:', solution())  # Shortest possible passcode: 73162890


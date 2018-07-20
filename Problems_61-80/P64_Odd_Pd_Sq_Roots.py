'''
Problem: How many continued fractions of sqrt(N) for N ≤ 10,000 have an odd period?
(Where N is non-square)

The naive approach to solving this question would be to narrow your focus to each term in
the sequence. Once we get a full repeat of a cycle, we know we have found the root's
representation, right? That is unfortunately not the case, because even sqrt(13) has four
1's before a 6 in its sequence. This will not be helpful.
Instead, in going about this problem it's best to find a pattern and go from there. You can
quickly notice that after calculating each successive term in the sequence, we get
a number of the form a/(sqrt(n)-b). Then we take the floor of this number to get the next
term in the sequence, then subtract the two numbers and flip the result. Once we arrive at
a pair of a & b which match the initial a & b, we know the cycle will just repeat.
This will give us a relatively fast way to arrive at an answer.
'''
def gen_frac1(n):
    root = n**0.5
    a, b = 1, int(root)         # Initialize values of a and b
    beg = (a, b)
    cur = int(a/(root-b))       # Get the next term
    frac = [b]                  # Initialize with the first term
    next = ()
    while next != beg:          # Check if the next (a, b) is equal to the first
        frac.append(cur)        # Add the next term in the sequence.
        a = (n-b*b)//a
        b = a*cur-b
        cur = int(a/(root-b))
        next = (a, b)
    return frac                 # Returns the repeating sequence of terms, plus the initial
'''
The rest is as simple as adding up all the lengths of the cycles mod 2.
'''
def solution1(n):
    count = 0
    rationals = set(i*i for i in range(1, int(n**0.5)+1))
    for i in range(1, n+1):
        if i in rationals:
            continue
        count += (len(gen_frac1(i))+1)%2   # Add 1 because initial term is added to cycle
    return count
'''
And the following solution is the exact same as the first one, except instead of returning 
a list of terms, it only finds the total number of terms in the cycle. 
'''
def gen_frac2(n):
    root = n**0.5
    a, b = 1, int(root)
    beg = (a, b)
    cur = int(a/(root-b))
    count = 0                   # Initialize the term count
    next = ()
    while next != beg:
        count += 1              # Add 1 for each successive term
        a = (n-b*b)//a
        b = a*cur-b
        cur = int(a/(root-b))
        next = (a, b)
    return count

def solution2(n):
    count = 0
    rationals = set(i*i for i in range(1, int(n**0.5)+1))
    for i in range(1, n+1):
        if i in rationals:
            continue
        count += gen_frac2(i)%2   # Now no 1 needs to be added
    return count
'''
The second solution ends up being slightly faster due to saving memory, but the difference
is not substantial. 
'''
print('Fractions with odd period:', solution2(10000))  # Fractions with odd period: 1322

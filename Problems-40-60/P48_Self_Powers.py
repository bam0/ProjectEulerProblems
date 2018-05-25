'''
Problem: Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

For a language like python with nearly unlimited number sizes, we can simply compute
the entire sum and take it mod 10. It's almost like cheating.
'''
def solution1(n):
    return sum(k**k for k in range(1, n+1))%10**10
'''
We might as well do it the long way just to practice:
'''
def solution2(n):
    ten = 10**10                  # Initialize the 10^10 mod
    total = 0
    for i in range(1, n+1):
        add = i                   # Setting up for i^i
        for j in range(i-1):
            add = (i*add)%ten
        total = (total+add)%ten   # Make sure total keeps track of last 10 digits
    return total
'''
Unsurprisingly, the first solution is much faster, despite the numbers
getting extremely large. 
'''
print('Last ten digits:', solution1(1000))  # Last ten digits: 9110846700


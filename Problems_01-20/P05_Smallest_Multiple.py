'''
Problem: What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?

Equivalently, this question is asking to give the lcm of the set {1,...,20}.
The nice thing about the lcm, is that it's just the product over the gcd.
And the nice thing about the gcd, is that it has an incredibly fast algorithm
called the 'Euclidean Algorithm' which is implemented here:
'''
def gcd(a,b):
    if not b:                # If b is 0, we are done.
        return a
    return gcd(b,a%b)        # Otherwise keep going.

def lcm(a,b):
    return a*b//gcd(a,b)
'''
Another nice thing is that the lcm of all the elements in the set is also just
the pairwise lcm of each of the elements. This is due to the properties of the gcd
as well.
'''
def solution(n):
    cur = 1
    for i in range(2,n+1):
        cur = lcm(cur, i)    # Compute the pairwise lcm of all elements
    return cur

print('Smallest multiple:', solution(20))   # Smallest multiple: 232792560

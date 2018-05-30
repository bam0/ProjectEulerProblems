'''
Problem: For which value of p ≤ 1000, is the number of solutions maximised?
(p = perimeter of an integral right triangle)

This problem is really just a meatier version of problem 9 in disguise.
All we need to do is take what we already know about forming pythagorean triples
and apply it again to this problem.
First we need the lovely gcd:
'''
def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)
'''
Now we can code out the solution. We first initialize a dictionary
with each number in the range of the perimeter. Then we look for a primitive
pythagorean triple, and when we have it, find all the possible perimeters that
are multiples of the same triple. Later we iterate over the dictionary and find
the perimeter with the highest value.  
'''
def solution(k):
    D = {}                              # Initialize the dictionary
    for i in range(1, k+1):
        D[i] = 0
    for m in range(1, int(k**0.5)//2):             # Bounded at around sqrt(k)/2
        for n in range(m, int(k**0.5)//2):
            if gcd(m,n)==1 and not (m%2 and n%2):  # Check if primitive
                p = p1 = 2*m*(m+n)                 # Get perimeter
                while p <= k:                      # Add all perimeters for
                    D[p]+=1                        # each primitive
                    p+=p1
    mx = (0,0)
    for key, val in D.items():                     # Find the maximum
        if val > mx[1]:
            mx = (key, val)
    print(mx)
    return mx[0]
'''
Trying to do this the brute force way could only lead to a lot of headache. 
'''
# (840, 11)
print('Max solutions at:', solution(1000))  # Max solutions at: 840


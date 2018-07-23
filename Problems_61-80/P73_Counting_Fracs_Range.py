'''
Problem: How many fractions lie between 1/3 and 1/2 in the sorted set
of reduced proper fractions for d ≤ 12,000?

This problem is an example of something simple to state, but very difficult to figure out
efficiently. What we can start off with is the most straightforward approach: For each
value of d, find all the reduced fractions n/d such that 1/3<=n/d<=1/2. By using the
same reasoning as in problem 71, we can efficiently find start and end points for which
numerators to check. Then we just need to add all numerators that satisfy gcd(n,d)=1.
First we bring in the gcd.
'''
def gcd(a, b):
    if not b:
        return a
    return gcd(b, a%b)
'''
And now we craft a simple, brute-force solution. 
'''
from math import ceil
def solution1(n):
    count = 0
    for d in range(5, n+1):
        start, end = int(ceil(d/3)), d//2  # Initialize start and end numerators
        for j in range(start, end+1):
            if gcd(j, d) == 1:             # Check if they are relatively prime
                count += 1
    return count
'''
This brute-force solution takes around the same time as the slower solution in problem 72. 
Of course we can optimize it significantly through other means.
The following is a recursive solution using a depth-first traversal of the Stern-Brocot tree
(see problem 73 overview), which enumerates the rational numbers. Starting with the adjacent
numbers 1/3 and 1/2 for d=3, we find all possible reduced fractions by using the same strategy
of calculating mediants used in problem 71. Each time a new denominator is calculated using
the mediant, if it is below the limit of 12,000, we keep going until we get something too
large. By the end, we will have checked between every possible fraction until the solution is
found. 
'''
def solution2(n):
    def counter(lim, left, right):
        med = left + right                   # Calculate the mediant
        if med > lim:                        # If above the limit, stop
            return 0
        else:
            tot = 1                          # Else, add to count
            tot += counter(lim, left, med)   # Check on the left
            tot += counter(lim, med, right)  # Check on the right
            return tot
    return counter(n, 3, 2)                  # Start with 1/3 and 1/2.
'''
Although this solution looks very clean and easy to read, due to python's limitations 
in recursive stack depth, finding a solution for 12,000 is not possible. We need to 
translate this recursive solution to an iterative solution using stacks if we want to
produce a solution to the problem given to us.
We start in a similar fashion to the above, with initial left and right values set to 3 and 2,
but we add an empty stack of about half the size of the limit. Again we start by calculating 
the mediant, then checking if it is above the limit. If it's not, we add to the count, 
work up the stack, keeping left the same, and changing right to the mediant. If it is, we work
down the stack, changing left to right, and right to the next value in the stack. Once the 
bottom of the stack is reached, the iterations stop. 
I must admit it's not the easiest algorithm to grasp. The following is translated from the 
algorithm given in the overview pdf of problem 73.   
'''
def solution3(n):
    count = top = 0
    stack = [0]*(n//2)                # Initialize empty stack
    left, right = 3, 2                # Initialize left and right to 1/3, 1/2
    while True:
        med = left + right            # Calculate the mediant
        if med > n:                   # Check if greater than limit
            if top > 0:
                left = right          # Move closer to 1/2
                top -= 1
                right = stack[top]    # Traverse down the stack
            else:                     # If at bottom of stack, stop
                break
        else:
            count += 1
            stack[top] = right        # Add to top of stack
            top += 1
            right = med               # Keep left constant, but shift right
    return count
'''
While this algorithm is still not very fast, it is enough to get the job done within a few
seconds. A more sophisticated approach is necessary to generate a solution in sub-linear 
time, but we will not go into it here. As mentioned previously, the overview of problem 
73 on Project Euler's site will give a comprehensive explanation of various methods of
solving this problem, including the optimal one.  
'''
print('Number of fractions in range:', solution3(12000)) # Number of fractions in range: 7295372


'''
Problem: Consider quadratic Diophantine equations of the form x^2 – Dy^2 = 1.
Find the value of D ≤ 1000 in minimal solutions of x for which the largest
value of x is obtained.

The simplest way to look at this problem is for each D, we start at y=1, working our
way up until we find a value of 1+Dy^2 which is equal to a square.
So how can we quickly check that we've found a square? The easiest way is to take the floor
of the square root, then square it and check if it is equal to the original number.
'''
def is_square(n):
    r = int(n**0.5)
    return r*r == n
'''
Then we implement what was stated above:
'''
def find_min(d):
    y = x = 1              # Start with y=1
    while x:
        x = 1+d*y*y        # Check if 1+Dy^2 is square
        if is_square(x):
            return x
        y += 1
'''
Finally, we find all of the squares, and check which value of D gives the largest minimum.  
'''
def too_slow(n):
    mx, ret = 1, 1            # Initialize maximum x and d values
    for d in range(1, n+1):
        if is_square(d):
            continue
        cur = find_min(d)
        if cur > mx:          # Check if greater than maximum
            mx, ret = cur, d
    return ret
'''
As the function's title implies, it's a bit too slow to get us a solution. And by a bit,
I mean we would all be dead long before then. The value of D=61 alone is 10 digits. And
the maximal value is 38 digits long! This method would never work, so we need to think of
something new.
As it turns out, we can utilize our solutions to the previous two problems to solve this
one! If we are given a number x/y ~ d^0.5, we square to get x^2/y^2 ~ d, and then rearrange
to get x^2-dy^2 ~ 0. And if d is non-square, and x/y is a close approximation for d^0.5, 
we would expect that we will eventually arrive at x^2-dy^2 = 1 for closer and closer 
rational approximations. And how do we find these approximations efficiently? By using the
cycle-finder from problem 64, along with the approximation calculator from problem 65. 
First we bring back our cycle-generating function.  
'''
def gen_frac(n):
    root = n**0.5
    a, b = 1, int(root)
    beg = (a, b)
    cur = int(a/(root-b))
    frac = [b]
    next = ()
    while next != beg:
        frac.append(cur)
        a = (n-b*b)//a
        b = a*cur-b
        cur = int(a/(root-b))
        next = (a, b)
    return frac
'''
Next we write a function that takes in a list of terms for the continued fraction of
an irrational number, and calculates the resulting rational approximation working backwards.
This is very similar to the function created in problem 65.  
'''
def approx(L):
    num, den = L[-1], 1
    for x in L[-2::-1]:             # Work backwards through the list
        num, den = x*num+den, num
    return (num, den)
'''
And now we can optimize the brute-force algorithm used above, starting with the first 
rational approximation and working upwards. If we need to go beyond the end of the cycle
for a root, we just loop back around to the beginning. 
'''
def solve_diophantine(d):
    F = gen_frac(d)                  # Get the list of terms in the cycle (plus initial)
    temp = F[:2]                     # Start with firs two terms
    x, y = approx(temp)              # And the initial rational approximation
    idx, lgt = 1, len(F)-1           # Get the current index & length of the cycle
    while (x*x - d*y*y) != 1:        # Stop when the equation is satisfied
        temp.append(F[(idx%lgt)+1])
        x, y = approx(temp)
        idx += 1
    return x
'''
All that's left is to find the value of D that we are looking for. The solution is
the same as the slower one, just using the faster algorithm for solving diophantine 
equations created above.  
'''
def solution(n):
    mx, ret = 1, 1
    for d in range(1, n+1):
        if is_square(d):
            continue
        cur = solve_diophantine(d)
        if cur > mx:
            mx, ret = cur, d
    return ret

print('D with largest x:', solution(1000))  # D with largest x: 661

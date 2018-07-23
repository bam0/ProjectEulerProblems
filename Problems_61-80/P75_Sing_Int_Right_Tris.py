'''
Problem: Given that L is the perimeter of the triangle, for how many values of
L ≤ 1,500,000 can exactly one integer sided right triangle be formed?

It seems a bit comical to talk about lengths of wire bending to form a triangle
instead of just saying that we are working with perimeters. Regardless, we already have
all the tools we need to solve this problem, but we need to travel all the way back to
problem 39. That problem asked us to find the value of the perimeter with the most
different integer right triangles. Now this problem is asking us to find the total number of
perimeters with the least different (one) integer right triangles. In essence, this is
just a beefier version of problem 39 with a higher bound. All we have to do is slightly
modify our previous solution to fit this problem.
First we need the gcd function.
'''
def gcd(a, b):
    if not b:
        return a
    return gcd(b, a%b)
'''
For the solution, almost everything is the same as before. We iterate over values of 
m & n to generate primitive right triangles of the form m^2-n^2, 2mn, m^2+n^2. Then we 
get each perimeter, generating all its multiples up to the limit. For each perimeter, 
we either add it to the dictionary, or increase its value in the dictionary by one.
In the end, we count how many perimeters in the dictionary are unique.   
'''
def solution(limit):
    root = int((limit/2)**0.5)                      # Initialize root limit
    L = {}                                          # and perimeter dictionary
    for m in range(2, root+1):
        for n in range(1, m):
            if gcd(m, n)==1 and not (m%2 and n%2):  # Check if primitive
                per = p = 2*m*(m+n)                 # Calculate perimeter
                while p < limit+1:
                    if p in L:
                        L[p] += 1
                    else:
                        L[p] = 1
                    p += per                        # Generate multiples of the perimeter
    count = 0
    for key, val in L.items():
        if val==1:                                  # Check if perimeter is unique
            count += 1
    return count

print('Number of unique perimeters:', solution(1500000)) # Number of unique perimeters: 161667

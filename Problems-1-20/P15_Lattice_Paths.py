'''
Problem: How many routes are there from the top left to the bottom right
of a 20x20 grid only traveling down and right?

This problem seems like a good chance to implement a simple recursive algorithm.
Each time we are at a point in the grid, we have a choice of some number of down
moves and some number of right moves. Each time we decrement that move by one.
Let's see how it works:
'''
def num_paths(down, right):
    if down == right == 0:
        return 1
    total = 0
    if down:
        total+=num_paths(down-1, right)
    if right:
        total+=num_paths(down, right-1)
    return total
'''
The one major problem with this is that the numbers will be getting very
big very fast. This can cause an enormous recursive stack to form, taking quite 
a long time for larger values. By the time we get to a 13x13 by grid, performance 
is already very slow.
We need to think of another method.
One crucial fact to notice is that any point in the lattice can only be reached by 
the point above it or to its left. This means that any points on the top row or leftmost
column have only one possible route to reach them. If we initialize an array with
ones on the top row and left column, we can then iterate over each empty point, setting its
value equal to the sum of the points to its left and above it. 
This should significantly improve efficiency!   
'''
def solution1(n):
    n = n+1
    arr = [[1]*n]
    for i in range(n-1):
        arr.append([1]+[0]*(n-1))
    for row in range(1, n):
        for col in range(1, n):
            arr[row][col]+=arr[row][col-1]+arr[row-1][col]
    return arr[n-1][n-1]
'''
Lastly, we can use some slightly more complex math to arrive at the 
quickest solution. We know in an n x n lattice we can move to the right n times,
and down n times. We can represent this as a single word made up of D's and R's:
RRRDDDR...RRD like so. Now we just need to find all distinct permutations of this word.
There are 2n letters total, and n of each, which leads to the answer being (2n choose n).
Let's implement a choose function and finish this up:   
'''
def n_Choose_k(n, k):
    result = 1
    for i in range(k):
        result*=(n-i)/(k-i)      # Taken from the formula n!/k!(n-k)!
    return int(result)

def solution2(n):
    return n_Choose_k(2*n, n)    # Calculate (2n choose n)


print('Number of paths:', solution2(20))   # Number of paths: 137846528820





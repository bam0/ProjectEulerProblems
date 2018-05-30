'''
Problem: Find the maximum total from top to bottom by moving to adjacent numbers
in the given triangle.

Although the problem explicitly states that trying out every possible path will not
scale for larger triangles, working out this brute force approach can still be
educational. We will be employing a recursive solution testing out all possible paths
to start out.
'''
with open('1_Path_Sum', 'r') as file:
    nums = []                                 # Initialize the list of numbers
    for line in file:
        nums.append(list(map(int, line.strip().split())))   # Fill in our list with each row
'''
Here we employ a recursive approach, where we start out with i = j = 0. 
For each point, we add the maximal value of the two adjacent paths below it.
Eventually we will arrive back at the beginning and reach a solution. 
'''
def solution1(i=0, j=0):       # Start at nums[0][0]
    total = nums[i][j]
    if i==len(nums)-1:         # Stop if we reach the bottom
        return total
    return total + max(solution1(i+1, j), solution1(i+1, j+1))  # Add the maximal value
'''
Well that's great and all, but how will we go about this with larger triangles?
A brute force approach like the previous won't help us a bit. 
So how about we think about this a little deeper.
Working from the top, we know that regardless, both subsequent options must have the
first number added to them. Then from there, to get the max sum at a given point,
we just choose whichever number above has the higher value and add it. 
Eventually when we get to the bottom, we will have a collection of maximal path sums to
each given point. Finally, we take the max across all of those values.  
'''
def solution2():
    for i in range(1, len(nums)):
        nums[i][0]+=nums[i-1][0]         # Add the value above the left edge
        for j in range(1, i):
            nums[i][j]+=max(nums[i-1][j-1], nums[i-1][j])     # Add the maximal value above
        nums[i][-1]+=nums[i-1][-1]       # Add the value above the right edge
    return max(nums[-1])
'''
We will take care to use the same approach when we get to problem 67.
'''
print('Maximal path sum:', solution2())  # Maximal path sum: 1074

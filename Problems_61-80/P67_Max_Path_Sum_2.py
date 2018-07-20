'''
Problem: By starting at the top of the triangle and moving to adjacent numbers
on the row below, find the maximum sum from top to bottom.

Because this problem is essentially just an up-scaled version of problem 18, there
is not much to discuss. An optimized solution was already discussed in that problem,
so there is no need to go into detail here. All we need to do is create a new text file,
change the name of the file, and implement exactly the same algorithm.
'''
with open('2_Path_Sum', 'r') as file:
    nums = []                                              # Initialize the list of numbers
    for line in file:
        nums.append(list(map(int, line.strip().split())))  # Fill in our list with each row

def solution():
    for i in range(1, len(nums)):
        nums[i][0]+=nums[i-1][0]                           # Add the value above the left edge
        for j in range(1, i):
            nums[i][j]+=max(nums[i-1][j-1], nums[i-1][j])  # Add the maximal value above
        nums[i][-1]+=nums[i-1][-1]                         # Add the value above the right edge
    return max(nums[-1])

print('Maximum sum:', solution())  # Maximum sum: 7273
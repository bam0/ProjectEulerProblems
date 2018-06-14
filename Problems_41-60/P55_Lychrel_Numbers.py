'''
Problem: How many Lychrel numbers are there below ten-thousand?

The algorithm is very simple. Take a number, reverse its digits, add the
two together, then check if you have a palindrome. It's surprising that even after a billion
iterations, the number 196 produces no palindrome, and there is still no proof that it is
in fact a Lychrel number. Maybe one day there will be a mathematical proof classifying
these numbers, but for now we are only able to hypothesize.
The first solution we will look at will be a very straight-forward, brute-force approach.
First we'll need to create a helper function to reverse the digits of a number and add.
'''
def rev_add(n):
    return n + int(str(n)[::-1])
'''
And next we check if a number satisfied the Lychrel property up to 50 iterations. 
'''
def is_lychrel(n):
    i = 1
    while i < 50:
        n = rev_add(n)
        if n == int(str(n)[::-1]):  # Check if the number is a palindrome
            return False
        i += 1                      # Otherwise keep going
    return True
'''
For the first solution, we will just go from 1 to n, apply the previous
function to each number, then return the total count.  
'''
def solution1(n):
    count = 0
    for i in range(1, n):
        if is_lychrel(i):
            count += 1
    return count
'''
While this will still get the job done relatively quickly, we can improve efficiency 
by keeping track of numbers we already know are or are not Lychrel. 
The strategy we will now use is to keep a dictionary of all the numbers we have checked, 
where the value of each number is a 1 for Lychrel, and 0 otherwise. Each time we check a 
new number, we create a running list of all the numbers we end up checking. If any one of them
yields a palindrome, or is in the dictionary, we break the loop. After that, add each number
in the list to the dictionary with the value determined by the loop.  
'''
def check_lychrel(n, dct):
    cur = rev_add(n)
    L = [cur]                           # Initialize the list
    i = val = 0
    while i < 50:
        if cur in dct:                  # If in dct, break
            val = dct[cur]
            break
        if cur == int(str(cur)[::-1]):  # Check if palindrome
            val = 0
            break
        cur = rev_add(cur)
        L.append(cur)
        i += 1
    if i == 50:                         # Check if Lychrel
        val = 1
    for num in L:
        dct[num] = val                  # Add each number to the dictionary
    return val
'''
This way of checking will now give us an answer over 5x quicker than the previous solution.
The rest is essentially the same as solution1. 
'''
def solution2(n):
    nums, count = {}, 0
    for i in range(1, n):
        if check_lychrel(i, nums):
            count += 1
    return count

print('Number of Lychrel nums:', solution2(10000))  # Number of Lychrel nums: 249


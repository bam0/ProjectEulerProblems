'''
Problem: Work out the first ten digits of the sum of the following one-hundred
50-digit numbers.

Python makes a problem like this trivial, as integers can be of practically unlimited size.
We can simply add them all up, turn it into a string, and return the first 10 characters.
'''
with open('50_digits', 'r') as file:
    nums = list(map(int, file.read().split('\n')))   # Create the list of numbers

def solution1(n):
    total = sum(nums)
    return str(total)[:n]          # Get the first 10 digits
'''
But just for fun, let's also get an answer without converting to a string.
By doing some math, it can be observed that the maximum sum of 100 digits
would be 900 - '9' 100 times. Essentially, this means that we can ignore digits
past position 12 since they will not affect the first ten digits of the sum, as 
the previous digital sums would not be large enough. 
'''
def solution2(n):
    total = 0
    for num in nums:
        total+=num//(10**(50-(n+2)))    # Mod by 10^38 here to leave the first 12 digits
    return total//(10**4)               # Two extra digits on the front, and two added
                                        # to the end, so take them away.

print('First 10 digits:', solution2(10))  # First 10 digits: 5537376230

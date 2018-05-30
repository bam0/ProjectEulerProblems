'''
Problem: Find the sum of all the numbers that can be written
as the sum of fifth powers of their digits.

The largest a digit could be would be 9, and 9^5 is about 60,000.
So if we had six 9's in one number, that would only give us 360,000.
Right off the bat we know we can limit our search to at most 360,000.
So let's do that. It should still not take too much time to compute.
First we will start out by crafting a couple of functions to help us out.
This one grabs the digits of a number and puts them in a list:
'''
def get_digits(n):
    L = []
    while n > 0:       # While we still have digits
        d = n%10       # Get the last digit
        L.append(d)
        n=(n-d)//10    # Cut the last digit off
    return L
'''
And the following computes the sum of the digits to the specified power. However,
we create a list first of fifth powers so we don't have to keep calculating them 
every time we call the function:
'''
fifths = [i**5 for i in range(10)]    # Create list of fifth powers of digits
def pow_sum(L, n):
    total = 0
    for i in L:
        total+=fifths[i]
    return total
'''
Finally all we have to do is implement both of our helper functions and 
check if the sum of the powers of the digits is equal to the number, then sum
over the resulting values. 
'''
def solution(n):
    total = 0
    for i in range(10, (n+1)*9**n):      # Go up to 9^5*6
        digs = get_digits(i)
        sm = pow_sum(digs, 5)
        if sm == i:                      # Check if it's valid
            total+=i
    return total
'''
Despite being "brute-force", this solution still
runs relatively quickly, even in python.
'''
print('Fifth power sum:', solution(5))   # Fifth power sum: 443839

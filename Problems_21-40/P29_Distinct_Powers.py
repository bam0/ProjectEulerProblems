'''
Problem: How many distinct terms are in the sequence generated by
a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

The obvious approach is to simply go through every single combination of
a and b and take their powers. Since there are only about 10,000 possibilities,
this shouldn't take much time to compute.
All we need to do is use a set to make sure we don't add any duplicate values.
'''
def solution1(n):
    nums = set()                   # Initialize the set
    for a in range(2, n+1):
        for b in range(2, n+1):
            nums.add(a**b)         # Add a^b to the set
    return len(nums)
'''
That was almost too easy, wasn't it? Surely we can figure out a more elegant way of 
doing this problem. 
Well it turns out we can simplify the process a lot by forgetting about actually calculating
all those powers. Instead, we focus on the exponents. Starting from 2, we calculate all its
possible exponents (2-100), then we take 2^2 and multiply all the existing exponents by 2.
We keep doing this for each power of 2 until we get to 2^6=64, the last power of 2 less than 
100. What we are left with is a set of all the possible exponents for powers of 2. 
We add this to our total and move on. When we get past 10, all the numbers we haven't 
checked will have all their exponents included, since their squares will be over 100. 
Taking all that into account, we get the following algorithm:
'''
def solution2(n):
    total, nums = 0, set()           # Initialize total & set of squares, cubes, etc.
    for i in range(2, n+1):
        if i in nums:                # If we've seen the number before, continue
            continue
        if i > n**0.5:               # If i > sqrt(n), we can just add all its exponents
            total+=n-1
            continue
        k, pows = 1, set()           # Initialize set of powers
        while i**k <= n:
            nums.add(i**k)           # Keep track of what we've seen before
            for j in range(2, n+1):
                pows.add(k*j)        # Add the power to the set
            k+=1
        total+=len(pows)             # Add the length of the set to the total
    return total
'''
The above solution can still be further optimized, but it runs rather quickly
up to n=1000. 
'''
print('Distinct powers:', solution2(100))  # Distinct powers: 9183


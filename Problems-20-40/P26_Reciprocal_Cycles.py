'''
Problem: Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.

This problem is certainly one of the more difficult ones, at least for the first
50 or so. There are many, many different ways of approaching this problem, but we
will only be looking at a couple here - one I created, and another I took from the
solution given by the OEIS.

This following solution simulates long division of the denominator into the numerator
(1) padded with 0's. The main issue I had with crafting it was the problem of leading
digits not associated with the cycle, and not adding enough digits during the cycle.
What I eventually had to do was create a list of values representing the extra digits
I missed, and also keep track of the index where the cycle started.
Although this was a major pain, it ended up working.
'''
def cycle_length1(d, n=1):
    if 320000%d==0:            # 2^9*5^4%d will get rid of all terminating decimals
        return 0
    while d > n:               # Get smallest power of 10 greater than d
        n*=10
    n = n%d
    nums, vals, count = [], [], 0  # Initialize the list of remainders, extra digits, and count
    while n not in nums:       # Check if we have repeated yet
        nums.append(n)
        while d > n:
            n*=10
        n = n%d
        k, extra = 10, 0       # Check for extra digits we missed
        while k*n < d:
            extra+=1
            k*=10
        count+=1+extra         # Add one because there will always be at least 1 digit
        vals.append(extra)
    i = nums.index(n)          # Get the index where the cycle starts
    if i!=0:
        return count - i - sum(vals[:i])   # subtract off the digits we don't need
    return count
'''
That was a bit of a convoluted solution, right? That may be true, but the following 
method is much clearer. All it does is check when d divides 10^a-10^b, for the smallest
powers a and b. Then it gives a-b. The reason this works is that any repeating decimal 
can be written as some number k/99..900...0, where k is the repeating cycle, and there 
can be any number of 9's and 0's. This algorithm just checks whenever that number is found. 
'''
def cycle_length2(d):
    if 320000%d==0:              # Check if d is terminating
        return 0
    else:
        a = 1                    # Initialize the exponent
        while True:
            for b in range(a-1, -1, -1):   # Try all exponents below a
                if (10 **a-10**b)%d==0:    # If we find the cycle, we're done
                    return a-b
            a+=1                 # Add 1 to a and keep trying
'''
While the second algorithm is much clearer, it is moderately slow for larger values
of d. So instead of using it, we will use my algorithm to generate the solution. 
The rest is simply finding the max. 
'''
def solution(n):
    mx_length = mx_num = 0
    for i in range(1, n+1):
        c = cycle_length1(i)
        if c > mx_length:
            mx_length, mx_num = c, i
    return [mx_num, mx_length]

print('Max num: {}, Max length: {}'.format(*solution(1000))) # Max num: 983, Max length: 982


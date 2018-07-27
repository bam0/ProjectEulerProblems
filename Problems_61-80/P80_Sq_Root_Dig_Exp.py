'''
Problem: For the first one hundred natural numbers, find the total of the digital
sums of the first one hundred decimal digits for all the irrational square roots.

To start off with, python makes this problem relatively trivial with its built-in
decimal library. Using this library, we can set the precision of decimals to be a
larger amount than usual, then add up the first hundred digits of each irrational
root.
First we will make a helper function that takes in a decimal of arbitrary precision and
returns the sum of the first 100 decimal digits. Using the re module is not required, but
makes the program a little simpler.
'''
import re
def get_sum(dec, n):
    r = re.sub(r'\.', '', str(dec))[:n]   # Remove the '.', limit to 100 digits
    return sum(map(int, r))               # Return the digital sum

'''
Now it's just a matter of applying the decimal module for each irrational square root.
We set the precision to be a little above 100 to eliminate rounding error.  
'''
import decimal as dc
def solution1(n):
    sq = set(i*i for i in range(2, int(n**0.5)+1))  # Generate set of squares
    dc.getcontext().prec = n+2                      # Set precision
    tot = 0
    for i in range(2, n):
        if i in sq:                                 # Check if non-square
            continue
        num = dc.Decimal(i).sqrt()
        tot += get_sum(num, n)                      # Add the digital sum
    return tot
'''
Despite the fact that this method is a very pythonic way to solve the problem, 
we can at least come up with something not relying on the built-in decimal library.
It turns out that there is quite an interesting way to solve this problem using a curious
algorithm called "square roots by subtraction". You start out with a=5*n and b=5. Whenever
a >= b, subtract b from a and add 10 to b, otherwise add two 0's to a and place a 0 in
between the last two digits of b. Each time b > a, b becomes 1 digit closer to approximating
sqrt(n). Therefore, all that needs to be done is count the total number of iterations it
takes until b > a for 100 times. The result will be the desired digital sum!    
'''
def sub_root(n, m):
    a, b = 5*n, 5               # Start with a=5*n, b=5
    sm = 0
    for i in range(m):
        cnt = 0                 # Count the number of iterations
        while a >= b:
            a, b = a-b, b+10
            cnt += 1
        sm += cnt               # Add to the total sum
        a, b = 100*a, 10*b-45   # Add 2 0s to a, put 0 in between last 2 digs of b
    return sm

def solution2(n):
    tot = 0
    st = set(i*i for i in range(2, int(n**0.5)+1))
    for i in range(2, n):
        if i in st:
            continue
        tot += sub_root(i, n)
    return tot
'''
Amazingly, the second method produces the correct result only slightly slower than the first, 
and all that was needed were very basic mathematical operations.    
'''
print('Digital sum total:', solution2(100))  # Digital sum total: 40886

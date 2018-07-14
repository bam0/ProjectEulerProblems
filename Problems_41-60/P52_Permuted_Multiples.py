'''
Problem: Find the smallest positive integer, x, such that
2x, 3x, 4x, 5x, and 6x, contain the same digits.

We'll be focusing on two methods of solving this problem here. The first
will be to count the number of occurrences of each digit in x, then match
them with the occurrences of the digits in the multiples of x.
The Counter built-in function will aid us in this process.
'''
from collections import Counter
def check_dict(n):
    n_dct = Counter(str(n))
    for i in range(2, 7):
        for key,val in Counter(str(i*n)).items():
            if n_dct[key]!=val:     # Check that the number of occurrences is the same
                return False
    return True
'''
One thing to note is that the solution is guaranteed to be a multiple of 3. 
The reason for this is that x must contain the same digits as 3x, which means the
sum of digits is the same, therefore x must be a multiple of 3. 
'''
def solution1():
    n = 3
    while not check_dict(n):
        n += 3
    return n
'''
Next we'll do things a little differently. Instead of counting the digits in
each number, we'll simply convert them into strings, sort them, and check if they
are equal. 
'''
def check_sort(n):
    s = sorted(str(n))
    for i in range(2, 7):
        t = sorted(str(i*n))
        if t!=s:
            return False
    return True
'''
This method gives us a solution nearly 5x faster than the previous. 
'''
def solution2():
    n = 3
    while not check_sort(n):
        n += 3
    return n
'''
But we still have room to optimize the previous solution. 
One important fact to notice is that we only need to check numbers up to 
the next power of 10 divided by 6. Otherwise, we would get numbers with more
digits than the starting number.   
'''
def solution3():
    i = 1
    while i:
        n = 10**i+2            # Start at a multiple of 3
        ten = 10**(i+1)//6     # Calculate the limiting value
        while n < ten:
            if check_sort(n):
                return n
            n += 3             # Check multiples of 3
        i += 1

print('Smallest permuted multiple:', solution3()) # Smallest permuted multiple: 142857

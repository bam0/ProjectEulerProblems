'''
Problem: Find the sum of all numbers, less than one million, which
are palindromic in base 10 and base 2.

The easiest way to approach this problem would be to go through every number, convert
it to binary, and check if it's the same as it is reversed. We can do that easily by
using the built-in binary-conversion function "bin(n)" and also by converting the decimal
number to a string. We can halve our search by noting that it would be impossible for an even
number to be palindromic in base 2, since there would be a zero at the end.
'''
def solution1(n):
    sm = 0
    for i in range(1, n+1, 2):                               # Iterate over odd #'s
        base10, base2 = str(i), bin(i)[2:]                   # Convert to string & binary
        if base10 == base10[::-1] and base2 == base2[::-1]:  # Check against the reversed string
            sm+=i
    return sm
'''
This actually runs in a decently short amount of time, but for higher values
it is highly inefficient. What if we did the same thing without using string 
conversions? 
We can actually construct the reverse of a given number in any base without 
too much effort. All we need to do is keep dividing out by the base and adding
it to our result. The following algorithm shows how it's done:
'''
def is_pal(n, base):
    result = 0                         # Start with empty result
    k = n
    while k > 0:
        result = result*base + k%base  # Shift result to the left and add next num
        k//=base                       # Divide out by the base and repeat
    return n == result                 # Check if they are the same
'''
Now we implement virtually the same solution as before:
'''
def solution2(n):
    sm = 0
    for i in range(1, n+1, 2):
        if is_pal(i, 10) and is_pal(i, 2):
            sm+=i
    return sm
'''
This solution is actually more than twice as slow as before. 
We really need to figure out a way to make things run more efficiently. 
So how about we actually construct palindromes in one base, and then just
check if they are palindromes in the other? This would cut down the
total number of checks by a lot.
To construct a palindrome in base 2, we can actually take advantage of 
bit shifting to make our lives easier. We start out with a binary number
equal to n, then depending on whether or not we want an even or odd
palindrome, we shift the bits of n to the right. Then we successively shift
the result to the left while shifting n to the right, collecting each 
binary digit as we go along.
'''
def base2_pal(n, odd):
    result = n
    if odd:                               # If we want an odd pal, shift right
        n >>= 1
    while n > 0:
        result = (result << 1) + (n & 1)  # Shift result left, add digit
        n >>= 1                           # Shift n to the right
    return result
'''
Now all we have to do is construct all of our odd and even palindromes in 
base two and check if they are also palindromes in base 10. 
'''
def solution3(n):
    sm = 0
    i = pal = 1                    # Initialize index, base 2 pal
    while pal < n:
        if is_pal(pal, 10):        # Check if also base 10 palindrome
            sm += pal
        i += 1
        pal = base2_pal(i, True)   # Generate the next palindrome
    i, pal = 1, 3                  # Initialize even palindromes
    while pal < n:
        if is_pal(pal, 10):        # Repeat the same process
            sm += pal
        i += 1
        pal = base2_pal(i, False)
    return sm
'''
Now our solution runs much, much faster! 
'''
print('Double-base sum:', solution3(1000000)) # Double-base sum: 872187


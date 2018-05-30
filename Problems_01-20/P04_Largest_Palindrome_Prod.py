'''
Problem: Find the largest palindrome made from the product of two three digit numbers.

This problem is deceptively straightforward. For a while I was trying to do some
calculations by factoring the palindromes, only to find the solution staring me in
the face. What we need to do is simply 'brute force' it, but in a considerably more
efficient manner.
First we start with making a palindrome generator.
'''
def palindrome_gen(n):
    return 1000*n+int(str(n)[::-1])       # Create the palindrome
'''
Now for the interesting part. All we are doing is checking if each number from 999
down to sqrt(palindrome) divides the palindrome. If the number goes below this target,
the other factor would have to be >3 digits by default.  
'''
def is_palindrome_prod(n):
    pal = palindrome_gen(n)
    cur, target = 999, int(pal**0.5+1)    # Current and target values
    while cur>=target:
        if not pal%cur:                   # Check if cur divides pal
            print('Largest PalProd is:')
            print(pal//cur, '*', cur, '=', pal)
            return True
        cur-=1
    return False

def solution(n=999):
    while (n > 99):
        if is_palindrome_prod(n):          # Now just check for the largest one
            break
        n-=1

solution()     # Largest PalProd is: 913 * 993 = 906609

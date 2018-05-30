'''
Problem: Find the sum of all the even Fibonacci numbers below 4,000,000.

This problem gives us a straightforward application of python's powerful same-line
variable assignment. We simple apply the formula f(n) = f(n-1) + f(n-2) for generating
Fibonacci numbers until the given limit.
'''
def solution1(n):
    total, a, b = 0, 1, 2  # Initialize the sequence
    while(a<n):
        if a%2==0:
            total+=a
        a, b = b, a+b      # Apply the formula: a -> b, b -> a + b
    return total
'''
However, we are not quite done yet. There is a slight optimization we can make, with the
knowledge that the sequence is always O E O O E O O E ... where O=Odd and E=Even. This
renders the usage of an if-statement moot since we will always know when an even number 
occurs. All we have to do is apply the formula and group terms:
'''
def solution2(n):
    total, a, b = 0, 2, 3   # Initialize at the the first even term
    while(a<n):
        total+=a
        a, b = a+2*b, 2*a+3*b    # Group terms to generate all even Fibonacci numbers
    return total

print('Sum:', solution2(4000000))  # Sum: 4613732

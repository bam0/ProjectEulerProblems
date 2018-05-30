'''
Problem: What is the sum of the numbers on the diagonals in a
1001 by 1001 spiral (formed by listing 1..(1001^2) rotating clockwise from the center)?

This question is really less about programming and more about pattern recognition.
What we can observe is that for each n by n spiral, the top right corner is always
an odd square. Using that fact, we can see that if the square is k^2, each of the
other corners must be k^2 - (k-1), k^2 - 2(k-1), and k^2 - 3(k-1). Adding that
together, we get 4k^2 - 6(k-1). So let's code it out:
'''
def solution1(n):
    total = 1                    # Start with just 1
    for i in range(3, n+1, 2):   # Go along each odd number
        total += 4*i*i-6*(i-1)   # Plug it into the formula
    return total
'''
However, why not go a step further and actually derive an explicit formula?
All we need to do is use two other formulas: 1 + 3 + ... + (2n-1)^2 = n(2n+1)(2n-1)/3
and 2 + 4 + ... + (2n-2) = n(n-1). 
Combining the previous equation with these two equations and doing some algebra, we 
get the following result:
'''
def solution2(n):
    n = (n+1)//2
    return 4*n*(2*n+1)*(2*n-1)//3 - 6*n*(n-1) - 3

print('Spiral sum:', solution2(1001))  # Spiral sum: 669171001


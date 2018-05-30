'''
Problem: Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.

Let's start it with a very straightforward and simple approach to this problem.
Just add up all the numbers 1 to 100, square it, and take away all the squares next.
'''
def solution1(n):
    result = 0
    for i in range(1, n+1):          # Find the sum
        result+=i
    result*=result                   # Square it
    for i in range(1, n+1):
        result-=i*i                  # Take away the squares
    return result
'''
But we could do all the operations from the previous approach in one
line by using list comprehensions!
'''
def solution2(n):
    return sum([i for i in range(1,n+1)])**2-sum([i*i for i in range(1, n+1)])
'''
Yet, with a bit of math knowledge we can avoid all of that summing and squaring business
altogether. We just need to apply the formula for the sum of squares n(n+1)(2n+1)/6 and 
the square of the sum (n(n+1)/2)^2 and do a little algebra to arrive at the following:
'''
def solution3(n):
    return n*(n+1)*(3*n**2-n-2)//12

print('Difference:', solution3(100))    # Difference: 25164150


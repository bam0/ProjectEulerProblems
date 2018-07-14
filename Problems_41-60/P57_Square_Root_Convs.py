'''
Problem: In the first one-thousand expansions (of sqrt(2)), how many fractions
contain a numerator with more digits than the denominator?


Developing an efficient algorithm for this problem first requires some algebraic
calculations. If we let our initial fraction be a/b, we get the next term a'/b' by
taking the expression 1 + 1/(1+a/b) = (a+2b)/(a+b). Since we know the first term in
the sequence is 3/2, we can generate the next thousand terms by using this iterative
procedure. This will make finding the solution quick and simple.
For the first solution, we find out if the numerator is longer than the denominator by
converting both numbers to strings and comparing their lengths.
'''
def solution1(n):
    a, b = 3, 2
    count = 0
    for _ in range(n-1):
        a, b = a+2*b, a+b
        count += len(str(a)) > len(str(b))  # Compare length using strings
    return count
'''
But in this next solution, we implement something slightly more clever. We'll keep
everything the same, except for determining the lengths of the numerator and denominator. 
Here we calculate the rounded value of each number log10, which gives a much quicker way
of comparing lengths for larger values. 
'''
import math
def solution2(n):
    a, b = 3, 2
    count = 0
    for _ in range(n-1):
        a, b = a+2*b, a+b
        count += int(math.log10(a)) > int(math.log10(b))  # Compare lengths using log10
    return count
'''
Although the difference between the two solutions is minimal for the value of 1000 given to
us in the problem statement, the second solution is exponentially faster for larger values. 
'''
print('Number with more digits:', solution2(1000))  # Number with more digits: 153



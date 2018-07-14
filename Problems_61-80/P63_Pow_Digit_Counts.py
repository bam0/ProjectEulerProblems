'''
Problem: How many n-digit positive integers exist which are also an nth power?

With a bit of reasoning, this problem could potentially be done manually with a calculator.
Since all nth powers of 10 are n+1 digits, so are all numbers greater than 10. Thus our
range of possibilities is only powers of the numbers 1-9. All we need to do is check the
nth powers of each number until the number of digits falls below n.
'''
def solution1():
    count, i = 0, 1              # Initialize count, digit i
    while i < 10:
        n, k = 1, i
        while len(str(k)) >= n:  # Check if number of digits is at least n
            n += 1
            k *= i               # Generate the next power
        count += n-1             # Add the number of valid powers to count
        i += 1
    return count
'''
And like problem 57, we can calculate string lengths using log10. Although there is 
not much of a performance due to there being very few possibilities to check. 
'''
import math
def solution2():
    count, i = 1, 2
    while i < 10:
        n, k = 1, i
        while math.ceil(math.log10(k)) >= n: # Find the length of the number using log10
            n += 1
            k *= i
        count += n-1
        i += 1
    return count
'''
That's all there is to it.
'''
print('n-digit n-th powers:', solution2())  # n-digit n-th powers: 49

'''
Problem: Find the sum of digits in the numerator of the 100th convergent
of the continued fraction for e.

Like problem 64, we are working with continued fractions which represent a square root.
But unlike that problem, we are given the pattern for the continued fraction of e, and
then we are expected to find a given term in the sequence of best rational approximations.
Since we already know the pattern, we could just create a list of the first 100
terms, then work backwards to find out the resulting numerator of the best rational
approximation.
First let's establish a helper function for generating a list of the first n terms in the
sequence.
'''
def gen_e_lst(n):
    e = [2]                             # Start with 2
    for i in range(n-1):
        if i%3==1:                      # Generate each respective even number
            e.append((2*i+4)//3)        # every third time
        else:
            e.append(1)                 # Otherwise add 1
    return e
'''
At the end we'll need this function to give our needed sum of digits in the numerator.
'''
def sum_dig(n):
    return sum(map(int, str(n)))
'''
So how will we work backwards in order to come up with a solution, given the list of the first
100 terms in the continued fraction for e?
It's quite simple. We will initialize the numerator and denominator as the last term in the
list, and 1. To get each successive number, all we need to do is flip the current number, and
add the next term in the list. Finally, we will use the sum_dig function on the numerator. 
'''
def solution1(n):
    e = gen_e_lst(n)
    num, den = e[-1], 1
    for x in e[-2::-1]:
        num, den = x*num+den, num
    return sum_dig(num)
'''
However, there is actually a way we can derive an answer without the need for a list or 
working backwards. All we need to do is keep track of the last two numerators, then the 
next numerator will be the first plus the second multiplied by the current term in the 
continued fraction sequence for e. For example, we start with 2 and 3. Since the second
term in the sequence is 2, we generate the next numerator by taking 2+2*3 = 8.
This process is not limited to numerators; the same happens to the denominator. 
And likewise, this process is not limited to e. The same general formula works for other
irrationals.  
Now we are ready for a slightly more efficient solution.  
'''
def solution2(n):
    a, b = 2, 3                        # Initialize first two numerators
    for i in range(n-1):
        if not i%3:                    # If the next term is not 1, calculate its value
            a, b = b, a+b*(2*i+6)//3
        else:                          # Otherwise, it is 1
            a, b = b, a+b
    return sum_dig(a)

print('Sum of digits of numerator:', solution2(100))  # Sum of digits of numerator: 272




'''
Problem: What is the millionth lexicographic permutation of the
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

There are a total of 10! = 3,628,800 different permutations of the digits 0-9.
So potentially, we could just generate every single permutation of these digits
and look for the millionth one, right? Python makes this easy with the built in
library 'itertools' containing many useful functions.
One of these is of course a permutation generator.
'''
import itertools as it
'''
The permutation function will give us a massive list of all the permutations of 
the digits 0-9, represented as tuples. 
'''
def solution1(n):
    perms = list(it.permutations(['0','1','2','3','4','5','6','7','8','9']))
    return ''.join(perms[n-1])       # Join the millionth permutation together.
'''
This is fine for the purposes of this problem, but it isn't very efficient. 
What can we do to make things faster? 
Well, we know that there are a total of 3.6 million permutations, so the millionth one will
be a little over a quarter of the way through the list. 
But how can we quantify this precisely to produce an algorithm? 
'''
def factorial(n):             # Borrow the factorial function to help us
    if n < 1:
        return 1
    return n*factorial(n-1)
'''
What we need to do is to make a list of the digits 0-9, then select them over successive
iterations and pop them from the list. To explain more precisely, say we are picking the
first digit. We know there will be 9!=362880 numbers starting with 0, another 362880 with 1, 
and so on. So the first digit must be 2. Then we take what's left and repeat the process
with 8! and so on until we get to 0.
This will be easier to understand simply by taking a look at this algorithm:
'''
def solution2(n):
    n-=1                  # Shift index of n back by 1 (1st iteration should return 012..9)
    digits = ['0','1','2','3','4','5','6','7','8','9']
    result = ''
    for i in range(9, -1, -1):        # Go backwards from 9! to 0!=1
        f = factorial(i)
        result+=digits.pop(n//f)      # Pop out the element at the given index and add it
        n-=f*(n//f)                   # Subtract and get what's left for the next iteration
    return result
'''
This essentially runs in near constant time, as opposed to calculating over 3.6 million
permutations!
'''
print('Millionth permutation:', solution2(1000000))  # Millionth permutation: 2783915460

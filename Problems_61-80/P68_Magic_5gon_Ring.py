'''
Problem: Using the numbers 1 to 10, and depending on arrangements, it is
possible to form 16- and 17-digit strings. What is the maximum 16-digit
string for a "magic" 5-gon ring?

Just by the pigeonhole principle, we know that if there were to be a solution, the maximum
possible starting digit would be 6. The outer numbers would be 6-10 and the inner numbers
would be 1-5. Working from here, it is actually possible to use a little bit of deductive
reasoning to come up with the solution by hand. But for the sake of keeping everything
programmable, we will also find the solution here.
What we can do is find all the permutations of 7-10 (with 6 appended to the front) and
then check each of these possibilities with all the permutations of 1-5. Once we get
something that satisfies the "magic" property, we check if it is indeed the max.
First we can import itertools to quickly calculate permutations.
'''
import itertools as it
'''
Now we will create two helper functions that will return the permutations from 1-5, and
the permutations from 6-10 with a leading 6. 
'''
def one_to_five():
    perms = it.permutations([1,2,3,4,5])
    return list(perms)

def six_to_ten():
    perms = it.permutations([7,8,9,10])
    perm_lst = list(perms)
    for i in range(len(perm_lst)):
        perm_lst[i] = (6,) + perm_lst[i]  # Add 6 to the front of each 7-10 permutation
    return perm_lst
'''
Next we create another helper function that takes in the outer tuple and the inner tuple of 
numbers and returns if they satisfy the magic property. Here, the outer and inner tuples
of numbers have a one to one correlation, and the first number in the outer tuple is the
minimum.  
'''
def check_magic(tup1, tup2):
    sm = tup1[0] + tup2[0] + tup2[1]         # Get the first sum
    for i in range(1, 5):
        tmp = tup1[i]+tup2[i]+tup2[(i+1)%5]
        if tmp != sm:                        # Check if each sum is the same as the first
            return False
    return True
'''
And for the final helper function, we take in two tuples satisfying the magic property
and print out the 5-gon in the format specified in the problem. 
'''
def magic_string(tup1, tup2):
    s = ''
    for i in range(5):
        s += str(tup1[i])+str(tup2[i])+str(tup2[(i+1)%5])
    return s
'''
At last, we can write the final few lines of code to bring everything together into 
a solution. 
'''
def solution():
    inner = one_to_five()
    outer = six_to_ten()
    mx = ''                                 # Initialize the maximal string
    for i in inner:
        for o in outer:
            if check_magic(o, i):           # If valid, generate the 5-gon string
                cur =  magic_string(o, i)
                if cur > mx:                # Compare to the current max
                    mx = cur
    return mx

print('Maximum 16-digit string:', solution())  # Maximum 16-digit string: 6531031914842725

'''
Some may wonder that since we have the maximal 16-digit string, what is the maximal 17-digit
string? We could run through a similar style of deductive reasoning to narrow down the
possibilities, but here I thought it would be fun to simply find every possible magic 
5-gon and then find the largest 17-digit string.
Using a brute-force approach, we calculate every single permutation of 1-10, split it 
into two tuples, then determine if the tuples create a magic 5-gon. 
'''
def biggest_17():
    perms = it.permutations([1,2,3,4,5,6,7,8,9,10])
    mx = ''                                           # Initialize maximal string
    for perm in perms:
        outer, inner = perm[:5], perm[5:]             # Split perm into two tuples
        if min(outer) != outer[0]:                    # If the beginning isn't minimal, continue
            continue
        if check_magic(outer, inner):                 # Check the magic property
            m = magic_string(outer, inner)
            if len(m) == 17 and m > mx:               # Find the maximal 17-digit string
                mx = m
    return mx

print('Maximum 17-digit string:', biggest_17())  # Maximum 17-digit string: 28797161103104548

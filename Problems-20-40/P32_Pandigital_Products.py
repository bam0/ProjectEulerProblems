'''
Problem: Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital (All the numbers together
contain the digits 1-9).

One of the simplest approaches we can take for this problem would be to first
generate every single permutation of 9 digits, then check each to see if we can
form a pandigital product out of it. We can quickly narrow it down to two potential
candidates: 0 * 0000 = 0000, and 00 * 000 = 0000.
Why only these? 1) it would be impossible to form a three digit number from two other
three digit numbers, and 2) it would also be impossible to form a five digit number
using only 4 digits. So this is what we're left with.
Now we can use the built-in permutations function from itertools to help us check each
of these forms.
'''
from itertools import permutations
'''
Check the first form - 0 * 0000 = 0000:
'''
def check_one(tup):
    a = tup[0]                                            # Get the first digit
    b = sum(10**(4-i)*tup[i] for i in range(1, 5))        # Get the next 4
    c = sum(10**(4-i)*tup[i+4] for i in range(1, 5))      # And the final 4
    return c if a*b==c else 0

def check_two(tup):
    a = 10*tup[0]+tup[1]                                  # Get the first 2 digits
    b = sum(10**(3-i)*tup[i+1] for i in range(1, 4))      # The next 3
    c = sum(10**(4-i)*tup[i+4] for i in range(1, 5))      # And the last 4
    return c if a*b==c else 0
'''
Now all we have to do is check each permutation.
'''
def solution1():
    perms = list(permutations([i for i in range(1, 10)]))
    pans = set()                               # Initialize the set of pandigital products
    for p in perms:
        a, b = check_one(p), check_two(p)      # Check against each form
        if a:
            pans.add(a)                        # If it's of the 1st form, add it
        elif b:
            pans.add(b)                        # Or if it's of the second form
    return sum(pans)
'''
This solution is definitely convenient, but it's also pretty slow. We can of 
course do better. 
So how can we speed things up? Well, instead of checking each permutation, we could 
go the other direction and check if each product is pandigital. 
We'll first need to write a function that checks for this property. 
One way is to convert each number to a string, then match the sorted list of
its values to the list of the characters '1' to '9'. 
'''
def is_pan(a,b):
    s = str(a) + str(b) + str(a*b)
    return sorted(s) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']
'''
Now we just need to apply this function to get a solution. 
We can reduce the number of checks to those that produce a product less than 10,000, 
as well as starting out at values that would produce valid permutations. 
'''
def solution2():
    pans = set()                          # Initialize the set of products
    for a in range(2, 9):
        for b in range(1234, 10000//a):   # Go until the product is above 10,000
            if is_pan(a,b):
                pans.add(a*b)             # Add the valid products
    for a in range(12, 100):              # Do the same with the second form
        for b in range(123, 10000//a):
            if is_pan(a,b):
                pans.add(a*b)
    return sum(pans)
'''
The second solution is over 80x faster! We cut the number of cases to check
significantly by not computing all those permutations first. 
'''
print('Pandigital sum:', solution2())  # Pandigital sum: 45228

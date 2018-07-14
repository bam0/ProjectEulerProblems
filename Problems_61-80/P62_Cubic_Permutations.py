'''
Problem: Find the smallest cube for which exactly five permutations of its
digits are cube.

Potentially, this problem could be done by finding all the cubes of a given length and
then finding the smallest cube with the same digits as 4 others. However, there is a
better way.
The following solution creates two dictionaries, one for the ordered
strings of digits for each cube, and another for each cube. Each of the ordered strings
has a corresponding value of the smallest cube with those digits. On the other hand, each of
the cubes has a corresponding value of the number of cubes with the same digits.
Once the value of one of the cubes is five, the cube is returned.
'''
def solution1(n):
    perm_dct = {}                          # Dictionary of ordered digits
    cube_dct = {}                          # Dictionary of smallest cubes
    i = 1
    while True:
        cb = i**3
        perm = ''.join(sorted(str(cb)))    # Order the digits
        if perm in perm_dct:               # Check if digits already in perm_dct
            small_cb = perm_dct[perm]
            cube_dct[small_cb] += 1        # Add 1 to the number of permutations
            if cube_dct[small_cb] == n:    # Check if there are 5 cubes with the same digits
                return small_cb
        else:
            perm_dct[perm] = cb            # Otherwise add the permutation to this dictionary
            cube_dct[cb] = 1
        i += 1
'''
We could also modify the above solution to only use a single dictionary, where each string
of ordered digits is assigned a list. The list contains the smallest cube with the given 
digits, along with the total number of cubes. 
'''
def solution2(n):
    perm_dct = {}
    i = 1
    while True:
        cb = i**3
        perm = ''.join(sorted(str(cb)))
        if perm in perm_dct:
            perm_dct[perm][1] += 1
            cb_lst = perm_dct[perm]
            if cb_lst[1] == n:
                return cb_lst[0]
        else:
            perm_dct[perm] = [cb, 1]   # Create list with smallest cube, initialize total to 1
        i += 1
'''
Despite the fact that the second solution cuts out the need for another dictionary, it is still
slightly slower than the first.
'''
print('Smallest cube:', solution1(5))  # Smallest cube: 127035954683

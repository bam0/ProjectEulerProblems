'''
Problem: Find the next triangle number that is also pentagonal and hexagonal.
(Tn = n(n+1)/2, Pn = n(3n-1)/2, Hn = n(2n-1))

This problem is not too bad to solve if we utilize sets. The first way we could
solve it is by generating a large list of pentagonal numbers and hexagonal numbers, then
iterating over the triangle numbers until we find a match in both sets.
'''
def solution1():
    pents = set(n*(3*n-1)//2 for n in range(1, 50000))
    hexas = set(n*(2*n-1) for n in range(1, 30000))
    count = 0
    i = k = 1                         # Initialize the triangle numbers k
    while count < 2:
        i += 1
        k += i                        # k adds i to become a triangle number
        if k in pents and k in hexas: # Check if it's in each set
            count += 1
    return k
'''
However we can optimize the previous solution by getting rid of the triangle numbers
altogether, since all hexagonal numbers are odd numbered triangle numbers. 
Therefore we can just generate a set of hexagonal numbers, then iterate over
the pentagonal numbers until we have a solution. 
'''
def solution2():
    hexas = set(n*(2*n-1) for n in range(1, 30000))
    count = 0
    i = k = 1
    while count < 2:
        i += 3
        k += i
        if k in hexas:
            count += 1
    return k
'''
However, that is not the only way we could approach this problem. The previous ones 
relied on guessing on a range for the set and seeing what works. We could skip this
entirely by looking at the equation for the pentagonal numbers, plugging in the hexagonal
numbers, and checking whether or not they produce integers.
'''
def solution3():
    count = 0
    i = k = 1
    while count < 2:
        i += 4                                  # Create hexagonal numbers
        k += i
        if ((1+(24*k+1)**0.5)/6).is_integer():  # Plug them into the equation for pentas,
            count += 1                          # and check if they're integers
    return k
'''
Despite the simplicity of the third solution, the second solution is still slightly
faster. 
'''
print('Tri-Pent-Hex Number:', solution2())   # Tri-Pent-Hex Number: 1533776805

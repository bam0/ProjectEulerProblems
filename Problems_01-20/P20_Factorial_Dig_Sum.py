'''
Problem: Find the sum of the digits in the number 100! (100 factorial)

This problem will be very similar to problem 16, where we summed the digits of
the number 2^1000. The first solution will be a near exact copy of that solution -
all we have to do is write a short factorial function.
Generating the factorial of a number is one of the most common ways to introduce
the concept of recursion, so let's do it:
'''
def factorial(n):
    if n==1:                   # When we get to 1, stop.
        return 1
    return n*factorial(n-1)    # Take the number and multiply it by (n-1)*(n-2)...

def solution1(n):
    return sum(list(map(int, str(factorial(n)))))
'''
And again like problem 16, let's try to implement the same solution, but on the list
representation of the digits of the number. 
First to make things easier on ourselves, we create a helper function which takes in two
lists of digits and adds the second list to the first. This will simulate the operation of
addition on two numbers. 
For this function, we will be taking advantage of python's interpretation of negative 
indices. For a list of length n, -1 represents n-1, -2 for n-2, and so on. 
We will work our way backwards adding each successive digit. 
'''
def add(lst1, lst2):
    r, j = 0, -len(lst2)-1           # r = remainder, j = beginning of lst2
    for i in range(-1, j, -1):       # Go backwards from the end -> start of lst2
        r, lst1[i] = divmod(r+lst2[i]+lst1[i], 10)     # Add the digits, get the remainder
    while r and j >= -len(lst1):     # If r>0 and we're not at start of lst1, keep going
        r, lst1[j] = divmod(r+lst1[j], 10)
        j-=1
    if r:
        lst1.insert(0, r)            # If we're at the beginning of lst1, insert the remainder
'''
The previous function may have been slightly complicated to interpret because of the negative
indices, but you should get the overall idea. 
Now to generate the factorial of each number. 
The key concept to understand here is that multiplication is essentially just successive 
addition. So to generate 4!, we start with 1, then do 1+1=2, then do 2+2+2=6, and finally 
6+6+6+6=24. This is how the following function will work. 
'''
def solution2(n):
    nums = [1]                  # Start at 1
    for i in range(2, n+1):
        temp = list(nums)       # Create a copy of the current list/number.
        for j in range(i-1):    # Add the copy to itself i-1 times
            add(nums, temp)
    return sum(nums)            # Get the sum of the digits

print('Factorial digit sum:', solution2(100)) # Factorial digit sum: 648


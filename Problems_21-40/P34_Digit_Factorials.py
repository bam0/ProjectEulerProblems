'''
Problem: Find the sum of all numbers which are equal to the sum
of the factorial of their digits.

It is very interesting that there exist numbers with this special property.
Unfortunately, there is not much of interest involved in writing a program to
check for it. All we have to do is make a list of the factorials of each digit,
then check the digits of each number against the sum of the factorials.
'''
def factorial(n):               # Our familiar friend the factorial
    if n<2:
        return 1
    return n*factorial(n-1)

facs = [factorial(i) for i in range(10)]  # Generate a pre-made list of values
def fac_sum(n):
    total = 0
    while n > 0:
        d = n%10               # Get the digit
        total+=facs[d]         # Add the factorial to the total
        n = (n-d)//10          # Rinse and repeat
    return total
'''
The only thing we have to do now is figure out an upper bound. Well, if we had
seven 9's in a row, the total of all those factorials would still only be 2.5 million, way
less than the 9.9 million needed. So we know anything above that would be unreachable. 
So let's go with 2.5 million to be safe as our bound, (although it takes over 5s).  
'''
def solution():
    curious = set()                     # Initialize set of numbers
    for i in range(10, facs[9] * 7):
        if i == fac_sum(i):             # Check if the number satisfies the conditions
            curious.add(i)              # Add it to the set
    print(curious)
    return sum(curious)
'''
The curious thing about these curious numbers is that there are only two!
Yeah, that's right, just TWO out of the entire number line.
'''
# {145, 40585}
print('Curious number sum:', solution())  # Curious number sum: 40730


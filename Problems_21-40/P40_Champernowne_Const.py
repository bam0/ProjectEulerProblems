'''
Problem: If d_n represents the nth digit of the fractional part,
find the value of the following expression: d_1 * d_10 * ... * d_1000000.

The first strategy we'll employ is a basic brute force approach. We'll keep
adding numbers to the end of a string until the length reaches above 1000000.
Then we simply convert each character at the specified position to an integer and
multiply them all together.
'''
def solution1(n):
    digits, length = '', 0
    for i in range(n):
        digits += str(i)                  # Add the number to our string
        length += len(str(i))
        if length > n:                    # Length above the limit, so we're done
            break
    prod = 1
    for k in range(7):
        prod*=int(digits[10**k])          # Multiply the specified digits together
    return prod
'''
But of course we can do way better than that. How about developing an algorithm
that quickly finds the digit we're looking for? Well, we note that for the 
first 9 numbers, only one digit is taken up. Then for the next 90, two digits are 
taken up. This pattern will continue, so we can create a list of the index positions 
that represent 9, 99, 999 and so on. Then we take the divmod of the position d minus 
the closest value in the list with the size of the numbers we're dealing with. 
The result of the division tells us which number to pull the digits from, and the 
modulus tells us how far to go up until we get the digit we want.
It's not easy to explain in words, so let's take a look:
'''
def find_digit(vals, d):                    # Take in position list vals, and digit# d
    i = 0                                   # i = length of numbers
    while vals[i] < d:
        i+=1
    go, up = divmod(d - vals[i-1], i)       # up = number of extra digits
    cur = 10**(i-1)+go-1                    # cur = number we pull digits from
    if up == 0:
        return int(str(cur)[-1])            # If no extra, pull from end of cur
    cur += 1
    return int(str(cur)[up-1])              # Otherwise, pull from next number up
'''
Now we just need to create a list of digit positions for 9, 99 ..., and find the digits
for each of the powers of 10 up to 1 million.  
'''
def solution2(n):
    vals, i, k = [], 0, 1
    while i < n:
        vals.append(i)                   # Append the digit position
        i += k*9*10**(k-1)               # Add next number of digits to i
        k += 1
    vals.append(i)
    prod = 1
    for j in range(7):
        prod*=find_digit(vals, 10**j)    # Find the product of the digits
    return prod
'''
The second solution runs in almost no time at all, vastly improving upon 
the previous one.
'''
print('Champernowne\'s const:', solution2(1000000)) # Champernowne's const: 210

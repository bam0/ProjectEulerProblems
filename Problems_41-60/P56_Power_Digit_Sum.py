'''
Problem: Considering natural numbers of the form, a^b, where a, b < 100,
what is the maximum digital sum?

In this problem, we will be looking at three different ways of arriving at the
same answer, with only minor differences between them.
The first solution will calculate all the powers of each number, then calculate the
sum of the digits using modular arithmetic, checking for the maximum value.
'''
def int_digit_sum(n):
    sm = 0
    while n > 0:
        n, k = divmod(n, 10)           # Divide out and add the last digit
        sm += k
    return sm

def solution1(n):
    mx_sum = 0
    for i in range(1, n):
        num = 1
        for j in range(1, n):
            num*=i
            sm = int_digit_sum(num)
            if sm > mx_sum:
                mx_sum = sm
    return mx_sum
'''
Next we'll do the same thing as solution 1, except now using string manipulation.
'''
def str_digit_sum(n):
    return sum(map(int, list(str(n))))

def solution2(n):
    mx_sum = 0
    for i in range(1, n):
        num = 1
        for j in range(1, n):
            num*=i
            sm = str_digit_sum(num)
            if sm > mx_sum:
                mx_sum = sm
    return mx_sum
'''
Finally we'll have a little fun. We'll now mimic previous problems where we used lists
for addition, except now we'll make a formula for list multiplication. 
First let's make a helper function which turns a number into a list. 
'''
def lst_num(n):
    return list(map(int, str(n)))
'''
For this algorithm, what we are mainly doing is keeping a running remainder r. We multiply
each digit by m, add it to r, then the current digit becomes the result mod 10, and r becomes
the result integer divide 10. If we are left with an r value at the end above 0, we simply 
append the digits of r to the front of our list N. 
'''
def mult(N, m):
    r = 0
    for i in range(-1, -len(N)-1, -1):     # Descend the list of digits
        r, N[i] = divmod((r+m*N[i]), 10)   # Change the current digit and remainder
    if r > 0:
        for num in lst_num(r)[::-1]:       # If r > 0, append the digits to the front
            N.insert(0, num)
    return N
'''
And finally, we proceed in the same manner as the previous two solutions. 
'''
def solution3(n):
    mx_sum = 0
    for i in range(1, n):
        pw_lst = [1]
        for j in range(1, n):
            mult(pw_lst, i)
            sm = sum(pw_lst)
            if sm > mx_sum:
                mx_sum = sm
    return mx_sum
'''
Out of all three, the second solution is actually the quickest, followed by the first, 
then the third. 
'''
print('Maximum digital sum:', solution2(100))  # Maximum digital sum: 972

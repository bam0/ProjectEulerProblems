'''
First we have the simplest way. All we do is check each number in the range 3<=i<=1000
for divisibility by 3 or 5, then add it to the total.
'''
def solution1(n):
    total = 0
    for i in range(3, n):
        if i%3==0 or i%5==0:
            total+=i
    return total
'''
This solution is the same as the above, but implemented in one line using list
comprehensions, the sum function, and a ternary operator. 
'''
def solution2(n):
    return sum([i if i%3==0 or i%5==0 else 0 for i in range(3, n)])
'''
Now we use a bit of math to solve this problem in O(1) time instead of O(n).
The sum of all numbers divisible by 3 or 5 is the same as the sum of all 
numbers divisible by 3, by 5, and less the numbers divisible by 15 due to the
principle of Inclusion/Exclusion. We use the formula for the sum of 1 to k 
k(k+1)/2 to finish off the calculation.
'''
def solution3(n):
    n = n-1
    a, b, c = n//3, n//5, n//15    #calculate each of the floors
    return 3*a*(a+1)//2 + 5*b*(b+1)//2 - 15*c*(c+1)//2    #sum from 1 to k -> k(k+1)/2


print('Sum:', solution3(1000)) #Sum: 233168

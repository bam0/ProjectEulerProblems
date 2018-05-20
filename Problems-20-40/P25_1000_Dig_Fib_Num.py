'''
Problem: What is the index of the first term in the Fibonacci sequence
to contain 1000 digits?

This is not the first time we've had a Fibonacci problem, so this should all
seem very familiar by now. However, this problem will present us with a nice lesson
on the reasons not to convert integers to strings.
'''
def solution1(n):
    a, b, count = 1, 1, 1      # Initialize the first 2 terms, and the count
    while(len(str(a))!=n):     # Check if a is 1000 digits
        a, b = b, a+b          # Apply the formula
        count+=1
    return count
'''
This will work, however for larger values of n - say 10,000 - this will take a very long time
to compute. So what could be more efficient. Three letters - M O D. We just need to take 
each number mod 10^(n-1). When a is not equal to its mod, then we know we're done!
'''
def solution2(n):
    a, b, count = 1, 1, 1
    mod = int(10**(n-1))
    while(a%mod==a):        # Check if a equals mod
        a, b = b, a+b
        count+=1
    return count
'''
This is actually a drastic improvement on the first solution, despite how they look
nearly identical. 
'''
print('1000 digit Fibonacci index:', solution2(1000)) # 1000 digit Fibonacci index: 4782

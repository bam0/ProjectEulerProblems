'''
Problem: What is the sum of the digits of the number 2^1000?

Again, for a language like python, a problem like this is simpler than it
should be. Our integers can be as large as we'd like, allowing us to compute the
solution in half a line of code:
'''
def solution1(n):
    return sum(list(map(int, str(2**n))))
'''
But what if we didn't have this luxury. Let's solve the same problem using a list of digits
instead. Depending on the remainder we get after each successive addition operation, we'll 
append the result mod 10 to the subsequent digit on the left, else insert it into the 
front of the list. Then we can sum over all the resulting digits. 
'''
def solution2(n):
    L = [2]                                # Initialize the list as [2]
    for i in range(1, n):                  # Iterate over each exponent
        r = 0
        for j in range(len(L)-1, -1, -1):
            r,a = divmod(2*L[j]+r, 10)     # Double each digit, calculate the remainder
            L[j]=a
        if r > 0:
            L.insert(0, r)                 # Insert the remainder to the front if > 0
    return sum(L)

print('Power digit sum:', solution2(1000))  # Power digit sum: 1366

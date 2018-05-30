'''
Problem: Find the thirteen adjacent digits in the 1000-digit number
that have the greatest product. What is the value of this product?

This problem isn't so bad, is it? All we have to do is go through the number in
increments of 13 and multiply each of the numbers together, then test if the
product is greater than the current max.
'''
with open('numbers', 'r') as nums:
    s = line = nums.readline().strip()      # Declare the string 's' containing the number
    while(line):
        line = nums.readline().strip()
        s+=line                             # Add lines to s
'''
Here is an implementation of just that:
'''
def solution1(n):
    num_list = list(map(int, s))            # Create a list containing each digit
    mx = 0
    for i in range(1000-n):                 # Go until you reach the last n digits
        val = 1
        for j in range(i, i+n):
            val*=num_list[j]                # Get the product
        if val > mx:
            mx = val
    return mx
'''
This is fine, certainly for the purposes of this problem, but how does it scale?
If you had to check a ton of digits, this would not be a very efficient solution,
since we are repeating a lot of multiplications. So how can we get around that?
On first thought, you'd think you could just keep a running product of thirteen numbers,
multiplying by the next and dividing by the first each time. 
However, we must account for the number 0, since we cannot afford to get a zero-division
error. So to get around that, we remove the 0's and group the digits accordingly.
Lastly, we find the maximal product for each group of digits if the length is >= 13.
'''
def find_max(L, n):
    val = 1
    for i in range(n):
        val*=L[i]                     # Generate the initial product
    mx = val
    for j in range(n, len(L)):
        val = (val*L[j])//L[j-n]      # Multiply by the next, divide by the first
        if val > mx:
            mx = val
    return mx

def solution2(n):
    new_list = s.split('0')           # Split the string by '0'
    new_list = [list(map(int, line)) for line in new_list]
    mx = 0
    for lst in new_list:
        if len(lst)<n:
            continue
        cur = find_max(lst, n)        # Implement the function above
        if cur > mx:
            mx = cur
    return mx
'''
Although the difference in time for this problem is negligible, if the number were
millions of digits long, the second solution would be much quicker. 
'''
print('Largest Product:', solution2(13))    # Largest Product: 23514624000


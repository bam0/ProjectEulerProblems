'''
Problem: Which starting number, under one million, produces the longest Collatz chain?

This is one of those beautiful problems in mathematics which is incredibly simple to
state, but nearly impossible to prove - like the twin prime conjecture, or the Goldbach
conjecture. Given any number n, if n%2==0 get n/2, else get 3n+1. Eventually you will
always (so it is conjectured) get to 1.
We could first approach this problem as one might suppose - check each number from 1 to
a million, plugging it into the recursive formula.
Let's see what happens:
'''
def Collatz(n):
    if n==1:                      # Get to 1 and we're done
        return 1
    elif n%2:
        return Collatz(3*n+1)+1   # 3n+1 if n odd
    else:
        return Collatz(n//2)+1    # n/2 if n even

def solution1(n):
    mx_length = mx_num = 1        # Initialize maximum chain and corresponding number
    for i in range(1, n+1):
        C = Collatz(i)
        if C > mx_length:         # Check if result > maximum
            mx_length, mx_num = C, i
    return (mx_num, mx_length)
'''
You should notice that this method is quite slow, taking anywhere from 30s to
a minute to compute. Surely we can do better than that. 
So what can we do to speed it up? Well, for starters, notice how we keep recomputing the
same Collatz numbers over and over again. We could instead keep track of them to prevent
this from happening by storing the values in a dictionary.
Let's see it in action: 
'''
Collatz_dict = {1:1}
def dynamic_Collatz(n):
    if n not in Collatz_dict:          # Check if in dictionary
        Collatz_dict[n] = dynamic_Collatz(3*n+1)+1 if n%2 else dynamic_Collatz(n//2)+1
    return Collatz_dict[n]             # Get back the result

def solution2(n):
    mx_length = mx_num = 1             # Initialize maximum chain and corresponding number
    for i in range(1, n+1):
        dC = dynamic_Collatz(i)
        if dC > mx_length:             # Check if result > maximum
            mx_length, mx_num = dC, i
    return (mx_num, mx_length)
'''
This solution is much quicker than the previous, taking over 25x less time. 
Yet another example of how dynamic programming and dictionaries/hashmaps can
improve efficiency. 
'''
print('Longest Collatz number:', solution2(1000000))  # Longest Collatz number: (837799, 525)

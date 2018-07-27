'''
Problem: Let p(n) represent the number of different ways in which n coins can be
separated into piles. Find the least value of n for which p(n) is divisible by one million.

On first glance, one might suppose we could just use the same strategy we've been using for
previous two problems to solve this one as well. Unfortunately, as the number of denominations
of coins grows larger, so does the run time. Using the same algorithm as before would
take an unfeasibly long amount of time. So, we will need to come up with something else.
If we could determine p(n+1) given P(1),...,p(n), surely that would greatly increase
computation speed.
One way to accomplish this uses Euler's pentagonal number theorem. By using the generalized
pentagonal numbers P_k = k(3k-1)/2 for k=-1,1,-2,2,..., we can derive a recurrence for p(n)
from its generating function. The recurrence goes: p(n) = p(n-1)+p(n-2)-p(n-5)-p(n-7)+p(n-12)
+p(n-15)-..., where p(n)=1 for n=0 and 0 for n<0. Thus, given a list of partitions from
0 to n-1, we can generate the partitions of n with relative ease.
First, let's create the algorithm.
'''
def p(n, parts):                                      # Take in n, and the partitions of n
    sm = 0
    i, j, k = 1, 2, 1
    while n-k > -1:                                   # Once we go past 0, we are done
        sm=sm+parts[n-k] if j%4==2 or j%4==3 else sm-parts[n-k]  # Alternate ++ and --
        i=i+j if j%2 else i-j                         # Alternate + and -
        k = i*(3*i-1)//2                              # Evaluate next pentagonal num
        j += 1
    return sm
'''
All that is left to do is to create a while loop to check when 1 million divides n. 
We can conserve a little memory by only keeping track of the values mod 1mil.   
'''
def solution(n):
    parts, i = [1], 0                # Initialize partition list, and index
    while parts[-1]%n:               # When p(n)%1mil==0, we are done
        i += 1
        parts.append(p(i, parts)%n)  # Keep track of p(n)%1mil only
    return i
'''
Despite this straightforward recurrence relation, the solution still takes nearly 10 seconds to
complete.   
'''
print('Least value of n:', solution(1000000))  # Least value of n: 55374
'''
As an added bonus, this algorithm can also be used to solve problem 76. 
For small n, they both take nearly the same amount of time to execute. 
'''
def problem76(n):
    parts= [1]
    for i in range(1, n+1):
        parts.append(p(i, parts))
    return parts[-1]-1

print('Another answer to 76:', problem76(100))  # Another answer to 76: 190569291

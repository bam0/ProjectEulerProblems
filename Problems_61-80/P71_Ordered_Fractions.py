'''
Problem: By listing the set of reduced proper fractions for d ≤ 1,000,000
in ascending order of size, find the numerator of the fraction immediately
to the left of 3/7.

Problems 71-73 all follow the same theme of finding out information about sets of reduced
proper fractions within a given denominator range. The simplest way to solve this problem
would be to create a set of reduced fractions, working up from d=1 to d=1mil, then look at
the number directly to the left of 3/7. However, because d is so large, there would be no
way to feasibly accomplish this in a reasonable amount of time.
Instead, we can note the fact that we really only need to check one fraction per d value.
If we have a fraction a/b < 3/7, then a < 3b/7. Taking floor(3b/7) will then give the
maximal numerator for a given b. Once we have the numerator, we can keep track of the maximal
fraction less than 3/7 by comparing it against the current max.
'''
def solution1(n):
    mn_val = mn_num = 0                 # Initialize max fraction & max numerator
    for d in range(2, n+1):
        if not d%7:                     # If gcd(d, 7) = 7, keep looking
            continue
        num = (d*3)//7                  # Find numerator
        cur = num/d
        if cur > mn_val:                # Compare against max fraction
            mn_val, mn_num = cur, num
    return mn_num
'''
Although this algorithm runs in linear time, we can improve it even further to get a
formula for finding the largest numerator in constant time. The only fact necessary to know
is that if we are given two fractions a/b and c/d with bc-ad=1, the fraction with smallest
denominator between them is (a+c)/(b+d). We are given 2/5 and 3/7 at the start, which satisfy
this property. Thus, the next fraction after 2/5 closest to 3/7 with smallest denominator is
(2+3)/(5+7) = 5/12. We can keep repeating this process over and over to get a formula for the
closest fraction to 3/7 as (2+3*k)/(5+7*k), where 5+7*k <= 1mil is maximized.  
'''
def solution2(n):
    k = (n-5)//7
    return 2+3*k
'''
Such a simple, yet elegant solution.
'''
print('Numerator to the left:', solution2(1000000))  # Numerator to the left: 428570


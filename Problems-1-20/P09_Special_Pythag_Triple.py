'''
Problem: There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

For the first approach, we brute force our way to an answer. Let's just keep checking
all the possible triplets for the pythagorean property and see what happens. We know
they have to be distinct, and we know they have to add up to 1000.
We can make things a little easier by first declaring c = 1000 - (a+b).
Next, we can make it so that a < b < c, and we can use that fact to avoid
checking a lot of duplicates.
This is still fairly inefficient, but let's see how it works.
'''
def solution1(n):
    for a in range(1, n//3):            # a cannot be more than 1/3 of n
        for b in range(a+1, n//2):      # b cannot be more than 1/2 of n
            c = n - (a+b)
            if a**2 + b**2 == c**2:
                print(a,'*', b,'*', c, '=', a*b*c)
                break
'''
So how do we do this efficiently? 
That's a good question. It turns out that there  is a wonderful way to generate 
pythagorean triples. It all comes down to a simple  formula:
            a = m^2 - n^2, b = 2mn, c = m^2 + n^2
The triple formed is 'primitive' if a, b, and c are coprime. This occurs when 
m and n are coprime and not both odd. 
Now all we need to do is implement this formula and calculate all the primitives where
2m^2 < 1000 --> m < sqrt(500) ~ 22. That's a lot less to check! 
Once we have a primitive, all we need to do is check if the sum divides 1000.
'''
def gcd(a, b):              # GCD function for calculating if coprime or not
    if not b:
        return a
    return gcd(b,a%b)

def solution2(n):
    limit  = int((n/2)**0.5)            # Establish the limit
    for i in range(1, limit):
        for j in range(i+1, limit):
            if gcd(i,j)==1 and not (i%2 and j%2):       # Check if we have a primitive triple
                if not n%(2*j*(i+j)):                   # Check if divisible by sum
                    a, b, c = j**2-i**2, 2*i*j, j**2+i**2     # Generate the triple
                    m = n//(2*j*(i+j))
                    print(a*m, '*', b*m, '*', c*m, '=', m**3 * a * b * c)
'''
Now the answer is found in practically no time at all. In fact, on this machine, this 
method was over 100x faster than the first. Wow! All it takes is implementing a well-known
formula for generating primitive pythagorean triples. 
'''
solution2(1000)    # 375 * 200 * 425 = 31875000

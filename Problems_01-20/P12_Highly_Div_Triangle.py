'''
Problem: What is the value of the first triangle number to have over five hundred divisors?

The thought of using a brute-force approaching to add up all the numbers up to n, and then
the same with division, sends shivers down my spine. There are many ways to speed this
process up, and the first and simplest way is to recognize the formula for triangle numbers
is n(n+1)/2, which we have already encountered back in problem 1.
The next thing to notice is that there is also a convenient formula for the number of
divisors a number has. It is the product of the exponents+1 of all the prime factors of the
number.
The final thing to note is that n and n+1 will always be relatively prime, so we can
just calculate the prime factors of each, and then plug them into our formula.
All of these optimizations will drastically increase the speed of our algorithm.
Let's take things one step at a time.
First up, we will initialize an array of primes for the divisor checking:
'''
def primes_sieve(n):
    a = [True] * n                         # Initialize the array of booleans
    a[0] = a[1] = False
    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for x in range(i*i, n, i):     # Set the non-primes to False
                a[x] = False
'''
Since we only have to check the divisors of n and n+1, the number of primes
necessary in our list need not be excessively high. We are using 5000 just to be safe.
'''
primes = list(primes_sieve(5000))
'''
Now let's create an algorithm for the number of divisors a number has:
'''
def num_div(n):
    prod = 1                          # Initialize the result
    if n==1:
        return prod
    for i in range(len(primes)):
        p = primes[i]
        if p**2 > n:                  # If p^2 > n, we know n must be prime!
            return 2*prod
        count = 0                     # Initialize the exponent
        while not n%p:
            count+=1
            n//=p                     # Keep dividing out by the prime
        prod*=(count+1)               # Remember to add 1 to the exponent
        if n==1:                      # n=1, so nothing more to see here
            break
    return prod
'''
We are almost there. All we have to do now is organize what we know
and formulate a solution:
'''
def solution(n):
    total, k = 0, 2         # Initialize total divisors, k = triangle number side length
    div2 = 1                # Initialize the number of divisors of k, k+1
    while total<n:
        total = 0
        div1 = num_div(k) if k%2 else num_div(k//2)    # Check if k is even
        total = div1*div2
        k+=1
        div2 = div1          # Shift the number of divisors up 1
    return (k-1)*(k-2)//2    # Offset the formula by two (k=3 after first iteration)

print('Highly divisible number:', solution(500))  # Highly divisible number: 76576500


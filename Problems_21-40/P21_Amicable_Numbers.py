'''
Problem: Evaluate the sum of all the amicable numbers under 10000.

So an amicable number is a number where the sum of the proper divisors
of the sum of its proper divisors is itself. A.k.a. S(a) = b, S(b) = a and
a!=b, where S(n) is the sum of divisors of n. That means we're going to need
some way of calculating the sum of divisors of a number.
We could simply divide all numbers up to n/2 and add them all up, but that would
be very inefficient.
Well we're in luck, because there happens to be a very handy formula:
    S(n) = (p_1^e_1-1)/(p_1-1)...(p_k^e_k-1)/(p_k-1) - n
where the p's are n's prime factors and the e's are their exponents+1.
The derivation of this formula comes from writing out the product of all possible
combinations of prime powers that divide the number.
But anyway, back to the problem.
First we'll need a list of primes. So let's use our prime sieve.
'''
def prime_sieve(n):
    L = [True] * n                         # Initialize the array of booleans
    L[0] = L[1] = False
    for (i, is_prime) in enumerate(L):
        if is_prime:
            yield i
            for x in range(i*i, n, i):     # Set the non-primes to False
                L[x] = False
'''
We'll only need primes up to just over 100 since sqrt(10000) = 100
'''
primes = list(prime_sieve(150))
'''
Now we need to implement the sum of divisors function, which will be the 
majority of the work for this problem. But in reality, this function is really 
not much different than the number of divisors function from problem 12. 
All we need to do is keep track of prime factors and exponents, and keep a 
running product according to our formula.
Then once all prime factors are found, we return the product minus the number.  
'''
def sum_div(n):
    prod, n_copy = 1, n                # Initialize the product and a copy of n
    if n==1:
        return 1
    for p in primes:
        if n < p*p:                    # Now we know n is prime, so add this to our product
            prod*=(n*n-1)//(n-1)
            break
        exp = 1                        # Initialize the exponent
        while not n%p:
            n//=p
            exp+=1
        prod*=int((p**exp-1))//(p-1)   # Plug p and exp into our formula
        if n==1:                       # When n is 1, we have no more primes to check
            break
    return prod-n_copy                 # Subtract off the copy of n
'''
Now we're ready to use our formula to generate a solution. 
First we'll try just calculating each of the sums, and if the 
sum is less than i and is amicable to i, we add it to our total.
This way we prevent repeats. 
'''
def solution1(n):
    total = 0
    for i in range(2, n):
        sm = sum_div(i)
        if sm < i and i == sum_div(sm):   # If the pair is amicable, add the sum
            total+=(sm+i)
    return total
'''
However we can slightly optimize the previous solution by instead using a dictionary.
The dictionary will keep track of the sum of divisors of each number, and if 
a number is listed as a value for the key for its sum of divisors, we add their sum to
the total. 
'''
def solution2(n):
    D, total = {}, 0               # Initialize the dictionary
    for i in range(2, n):
        sm = sum_div(i)
        if sm < i and sm!=1:
            if D[sm] == i:         # If we have an amicable pair, add their sum
                total+=(i+sm)
        D[i] = sm                  # Add the value to the dictionary
    return total

print('Sum of amicable numbers:', solution2(10000))   # Sum of amicable numbers: 31626

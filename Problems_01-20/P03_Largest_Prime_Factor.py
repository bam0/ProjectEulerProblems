'''
Problem: What is the largest prime factor of 600851475143?

Immediately we know that a brute force approach is going to fail. The number is 12
whole digits long! Well we can clearly rule out 2. So let's write a prime-checker for n>2,
and then keep dividing the number by primes until we find our max.
'''
num = 600851475143

def prime_checker(n):
    for i in range(3, int(n**0.5+1), 2):  # Increment up to sqrt(n) by 2
        if n%i==0:
            return False
    return True
'''
What we do here is keep dividing num by each prime until the remainder is something 
other than 1. When we reach 1, we know we're done.
'''
def solution1(n):
    mx = 1
    for i in range(3, int(n**0.5+1), 2):
        if prime_checker(i) and not n%i:    # Here 'not n%i' is the same as 'n%i==0'
            mx = i
            while(not n%i):
                n, r = divmod(n,i)    # Divmod(a,b) gives the tuple: (a//b, a%b)
                if r:                 # Again, here we are checking if r!=0
                    break
            if n==1:
                   break
    return mx
'''
So the previous solution returns the answer almost instantly, contrary to
what you'd initially expect. But we could have done it differently by
implementing the sieve of Eratosthenes. However, the first solution is actually 
over 15x faster because of the large amount of memory required to form the prime 
sieve's list.
'''
def primes_sieve(n):
    a = [True] * n                         # Initialize the array of booleans
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for x in range(i*i, n, i):     # Set the non-primes to False
                a[x] = False

def solution2(n):
    mx = 1
    sieve = primes_sieve(int(n**0.5+1))
    for i in sieve:
        if not n%i:                   # Here 'not n%i' is the same as 'n%i==0'
            mx = i
            while(not n%i):
                n, r = divmod(n,i)    # Divmod(a,b) gives the tuple: (a//b, a%b)
                if r:                 # Again, here we are checking if r!=0
                    break
            if n==1:
                   break
    return mx

print('Largest Factor:', solution1(num))   # Largest Factor: 6857

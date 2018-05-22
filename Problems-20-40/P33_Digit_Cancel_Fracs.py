'''
Problem: There are exactly four non-trivial examples of digit cancelling fractions,
less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

The wording for this problem could have been a lot better, but I assume by non-trivial
the poster meant that the fractions would be cancelling in a "diagonal" fashion, with
both digits being of the same value.
There is not a lot to this problem, other than gathering the digits we need to test, and
writing a helper function to simplify fractions. And really, the only thing we need to
simplify fractions is to divide out by the gcd.
'''
def gcd(a,b):               # Reusing the same gcd function as usual
    if b==0:
        return a
    return gcd(b, a%b)

def simplify(n, d):         # Take in the numerator and denominator
    g = gcd(n, d)
    return (n//g, d//g)     # Divide out by the gcd
'''
Now that we have this, all we need is to write a function that takes in a fraction
and returns if it satisfies the above criteria. 
'''
def check_combs(n, d):
    n2, d2 = n%10, d%10                             # Collect the ones digits
    n1, d1 = (n-n2)//10, (d-d2)//10                 # Collect the tens digits
    nd = simplify(n,d)
    if simplify(n1, d2) == nd and n2 == d1 or \
        simplify(n2, d1) == nd and n1 == d2:        # Compare the fractions with the initial
        return True                                 # fraction
    return False
'''
Finally, we need to iterate over all the possible numerators and denominators we could
have. First, we remove all 2-digit numbers with zeros in them, and then we iterate 
over all fractions less than one.
'''
def solution():
    fracs = []                                   # Initialize fraction list
    nds = list(filter(lambda x: x%10!=0, [i for i in range(11, 100)]))
    for n in range(len(nds)-1):
        for d in range(n+1, len(nds)):           # Iterate over all possible n/d combos
            if check_combs(nds[n],nds[d]):       # Check if they are valid
                fracs.append((nds[n],nds[d]))
    print(fracs)
    num = den = 1
    for frac in fracs:                           # Find the num/den of each fraction
        num*=frac[0]
        den*=frac[1]
    return simplify(num, den)[1]                 # Simplify and return the denominator

print('Digit-cancel Denominator:', solution())
# [(16, 64), (19, 95), (26, 65), (49, 98)]
# Digit-cancel Denominator: 100
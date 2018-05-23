'''
Problem: What is the largest 1 to 9 pandigital 9-digit number that can
be formed as the concatenated product of an integer with (1,2, ... , n)
where n > 1?

Let's start out by writing a short program that takes in an integer n and
a length k and multiplies n for each value in 1...k, concatenating the
result. Then it checks whether or not it is pandigital.
'''
def is_pan(n, k):
    s = ''                             # Initialize the string
    for i in range(1, k+1):
        s += str(n*i)                  # Concatenate the products
    return sorted(s) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']
'''
Since the problem gives us an example which starts with a 9, we can already
rule out any cases with a starting digit below 9. Furthermore, we can narrow
our search even more by thinking about the structure of the pandigital number.
We could have 0 00 00 00 00, 00 00 00 000, 000 000 000, or 0000 0000. 
The first form was already given to us. But the second and third forms would be
impossible with 90<n<100 or 900<n<1000, since the digits would get too large too
quickly. So that just leaves us with the final form - a four digit number, and 
its double. Now we hardly have to check anything!
'''
def solution():
    pans = set()                     # Initialize pandigitals
    for n in range(9123, 9877):      # Check from smallest to largest 4-digit
        if is_pan(n, 2):             # Check pandigital property
            s = ''
            for j in range(1, 3):
                s += str(n*j)
            pans.add(s)              # Add pandigital number to the set
    return max(pans)

print('Largest pandigital:', solution())  # Largest pandigital: 932718654


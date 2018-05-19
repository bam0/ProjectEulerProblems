'''
Problem: If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

To combat this problem, the only sensible approach is to create a hashtable/dictionary.
One possible way to do things would be to write out the words and attribute them to
their corresponding numbers. However, instead of writing out the full words, it will
be a bit less effort to simply designate each number to its word's length.
'''
D = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8,
     15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6,
     90:6, 100:7, 1000:8}
'''
Now that we've created our dictionary of values, let's work out the solution:
'''
def solution():
    total = 0                            # Initialize the return value
    for i in range(1, 100):
        if i in D:                       # Add up the values in D
            total+=D[i]
        else:
            total+=D[i-(i%10)]+D[i%10]   # Else combine the tens and ones digit values
    for i in range(100, 1000):
        a, b, c = i//100, i%100-i%10, i%10   # a,b,c represent each digit (b is 10x it's digit)
        total+=D[a]+D[100]               # Add 'one hundred', 'two hundred' etc.
        if not i%100:                    # If mod 100 = 0, keep going
            continue
        total+=3                         # Add 'and'
        if 0<(b+c)<21:
            total+=D[b+c]                # Add the rest if it's 1-20
            continue
        total+=D[b]                      # Add the tens digit
        if c:
            total+=D[c]                  # Add the ones digit
    return total+3+D[1000]               # Add 'one thousand'
'''
And just like that, we're done. Nothing too complex to explain here.
'''
print('Total letters:', solution())   # Total letters: 21124

'''
Problem: What is the total of all the name scores in the file?
(Where each name is scored as the product of its position in the sorted list
and the sum of the values (1-26) of each of its letters)

Besides a few handy built-in functions, this problem doesn't present us with a
lot of interesting material to learn. All we need to do is read the file, convert the
names into a list, enumerate the list, and multiply each name's index by its score.
'''
with open('names', 'r') as names:
    name_list = names.read()[1:-1].split('","')   # Get rid of all the quotes and commas
'''
In order to calculate the score for a letter, all we need to do is look at a table of 
ASCII values for letters. We see that 'A' has a value of 65, so we need to subtract 64 
from each letter's ASCII value to get that letter's score. 
We can accomplish this all by using the ord(char) function. 
'''
def solution():
    name_list.sort()                         # Sort the list
    sm = 0
    for (i, name) in enumerate(name_list):   # Match each name with its index
        score = 0
        for ltr in name:
            score+=ord(ltr)-64               # Calculate the letter's ASCII value
        sm+=score*(i+1)                      # Add 1 to i
    return sm

print('Name score total:', solution())   # Name score total: 871198282

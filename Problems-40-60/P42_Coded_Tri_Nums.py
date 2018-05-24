'''
Problem: How many of the two-thousand common words are triangle words?
(Sum of the letter values is a triangle number)

This problem is nearly identical to problem 22, except now we have to
check if the word score is in the set of triangle numbers.
First we read the file and create a list of the words:
'''
with open('words', 'r') as w:
    words = w.read()[1:-1].split('","')    # Remove unwanted characters
'''
Now we create a dictionary of the letter scores:
'''
vals = {}
for i in range(65, 91):
    vals[chr(i)] = i - 64      # Use the built-in chr() function
'''
Calculate the word score:
'''
def word_score(word):
    return sum(vals[ltr] for ltr in word)
'''
And finally create the set of triangle numbers and check if each word's
score is in the set.
'''
def solution():
    count = 0
    triang = set(i*(i+1)//2 for i in range(1, 32))   # upper limit ~20 Z's
    for word in words:
        if word_score(word) in triang:
            count+=1
    return count

print('Triangle word count:', solution()) # Triangle word count: 162

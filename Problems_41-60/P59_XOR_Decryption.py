'''
Problem: Decrypt the message in cipher.txt and find the sum of the ASCII values
in the original text, knowing that the encryption key is 3 lowercase letters.

This problem is deceptively simple. The fact that the explanation for the problem is
rather lengthy helps mask this, but it all really boils down to one question: In a
typical piece of text, what is the most common character that occurs? A quick search for
letter frequency in the English language will tell you it's the letter 'e'. However, this is
forgetting capital letters, symbols, and numbers, which are all still fair game. So what is
it then? It's used to separate every word we use. That's right, it's the space: ' '.
So considering the text given to us is filled with common English words, and the encryption
key is 3 letters, we can do a frequency test on every set of letters separated by 3 characters.
We then find the maximum of each set, XOR it with the ' ' character, and the result will
be the encryption key.
Once we have the encryption key, we can just XOR each value in the file with the encryption
key to return back the original file.
We start by making a list of each of the ascii values in the file.
'''
with open('cipher', 'r') as cipher:
    chr_lst = cipher.read().split(',')
    chr_lst = list(map(int, chr_lst))
'''
And now all we have to do is implement what was mentioned above in order to find the
solution. Using the built-in Counter object will make finding the occurrences of each
value quicker. 
'''
from collections import Counter
def solution():
    nums = []                                    # Initialize encryption key list
    for i in range(3):
        C = Counter(chr_lst[i::3]).items()       # Find the occurrence of every 3rd num
        nums.append(max(C, key=lambda x: x[1]))  # Find the maximum value
        nums[i] = nums[i][0] ^ ord(' ')          # XOR it with the space character
    total = idx = 0
    for n in chr_lst:
        total += n ^ nums[idx%3]                 # XOR with the encryption key and add
        idx += 1
    return total
'''
If done correctly, the encryption key will spell 'god', and the hidden text will be 
revealed to be the first chapter of the gospel of John from the Bible. 
'''
print('Sum of ASCII values:', solution())  # Sum of ASCII values: 107359

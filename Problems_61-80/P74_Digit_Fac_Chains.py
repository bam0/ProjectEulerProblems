'''
Problem: How many chains, with a starting number below one million,
contain exactly sixty non-repeating terms?

As is usual by now, we can first solve this problem by starting a chain and counting
how long it takes to repeat, for each number from 1 to 1 million. If the length of a
chain gets to 60, it gets added to the total count.
First, we will start out by making a global list corresponding to the value of the factorial
of each digit.
'''
def gen_facs(n):
    facs = [1]                # Start with 0! = 1
    for i in range(1, n+1):
        cur = facs[i-1]
        facs.append(cur*i)    # Append n*fac(n-1)
    return facs

facs = gen_facs(9)

'''
Now that we have a quick reference for each factorial, we can write a helper function 
to generate the sum of the factorials of a number's digits.
'''
def sum_fac_dig(n):
    sm = 0
    for x in map(int, str(n)):
        sm += facs[x]
    return sm
'''
And now that we have a factorial digit sum calculator, we can use it to
find the length of the cycle for a given number. All we need to do is initialize 
a set with the number n, then keep adding the resulting factorial digit sum to the
set until we get a repeat.  
'''
def chain_length(n):
    dig_set = {n}               # Initialize the set
    sm = sum_fac_dig(n)
    while sm not in dig_set:    # If in set, we are done
        dig_set.add(sm)
        sm = sum_fac_dig(sm)    # Get the next factorial digit sum
    return len(dig_set)
'''
All that needs to be done now is check all the values from 1 to 1mil for
all chains of length 60. 
'''
def solution1(n):
    count = 0
    for i in range(1, n):
        if chain_length(i) == 60:
            count += 1
    return count
'''
Unfortunately, the above is excessively slow, taking nearly one minute to complete. 
We will need to come up with a faster solution. 
What we can instead do is create a dictionary of numbers, where each corresponding value 
is the length of its chain. First we will create a global dictionary with all the 
loops that exists, as per the problem statement. We will need to add in 1, 2, 145, and
40585 as they are the only numbers which are equivalent to their factorial digit sums. 
'''
dct = {}
dct[169] = dct[363601] = dct[1454] = 3
dct[871] = dct[872] = dct[45361] = dct[45362] = 2
dct[1] = dct[2] = dct[145] = dct[40585] = 1
'''
Now we can optimize the previous brute-force approach by remembering which numbers have 
already been checked. Like before, we create a list of each sum we calculate. Once we
reach a number in the dictionary, we stop the loop. After that, each number in the list
is added to the dictionary with a value of the ending sum's value plus the number
of iterations following the number.  
'''
def get_length(n, a_dct):
    if n in a_dct:
        return a_dct[n]
    lst = [n]                               # Initialize list of checked values
    while lst[-1] not in a_dct:
        sm = sum_fac_dig(lst[-1])
        lst.append(sm)
    size, val = len(lst)-1, a_dct[lst[-1]]  # Calculate size of list and last sum's value
    for i in range(size):
        a_dct[lst[i]] = val+size-i          # Add each member of list to the dictionary
    return a_dct[n]
'''
And the rest is the same as before, with the faster algorithm implemented. 
'''
def solution2(n):
    count = 0
    for i in range(3, n):
        if get_length(i, dct) == 60:
            count += 1
    return count

print('Number of chains:', solution2(1000000))  # Number of chains: 402


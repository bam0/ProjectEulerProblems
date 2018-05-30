'''
Problem: What is the greatest product of four adjacent numbers in the same
direction (up, down, left, right, or diagonally) in the 20×20 grid?

If anything, this question is a good way to exercise your nested for-loop
skills. It can sometimes be difficult to keep track of which index is which,
but naming them 'row' or 'col' can make things easier on yourself.
First we create the array:
'''
with open('20_by_20', 'r') as file:
    arr = []
    for line in file:
        arr.append(list(map(int, line.strip().split())))    # Fill the array with numbers
'''
Now we will write four functions, one for each of the different possible combinations
of four adjacent numbers - rows, columns, slashes, and backslashes. 
'''
def max_row(n):
    mx = 0
    for row in arr:                      # Iterate over the rows
        for i in range(len(arr)-n):
            prod = 1
            for j in range(i, i+n):      # Check each set of four
                prod*=row[j]
            if prod > mx:                # Find the maximum
                mx = prod
    return mx
'''
This function is nearly identical to the previous one, except we can no
longer simply iterate over the rows. We'll need to add a column index.
'''
def max_col(n):
    mx = 0
    for col in range(len(arr)):             # Iterate over the columns
        for i in range(len(arr)-n):
            prod = 1
            for j in range(i, i+n):
                prod*=arr[j][col]           # Keep column fixed, iterate over rows
            if prod > mx:
                mx = prod
    return mx
'''
Now we'll need to keep track of our rows and columns. The row and col indices will 
tell us where to start from in the upper-left 16x16 square. Then we just add 1-4 to 
each index to form the backslash shape. 
'''
def max_backslash(n):
    mx = 0
    for row in range(len(arr)-n):
        for col in range(len(arr)-n):
            prod = 1
            for i in range(n):
                prod*=arr[row+i][col+i]   # Add 1-4 to the row and col indices
            if prod > mx:
                mx = prod
    return mx
'''
Finally we calculate the max of the slash, which is the same as backslash but with 
1-4 being added to the row indices in reverse. 
'''
def max_slash(n):
    mx = 0
    for row in range(len(arr)-n):
        for col in range(len(arr)-n):
            prod = 1
            for i in range(n):
                prod *= arr[row+n-i][col+i]    # Add 4-1 to the row, 1-4 to the col indices
            if prod > mx:
                mx = prod
    return mx
'''
Well now we're done... or so you'd think! Doesn't the code for the row/column and 
slash/backslash programs look nearly the same? Well, actually we are just performing the
same process, but on the matrix rotated 90 degrees. So let's implement a short matrix-
rotation algorithm to reduce repeated code. 
'''
def rotate_array(M):
    n = len(M)
    for i in range(n//2):
        for j in range(n-1-2*i):
            M[i][i+j], M[i+j][n-i-1], M[n-i-1][n-(i+j)-1], M[n-(i+j)-1][i] = \
            M[n-(i+j)-1][i], M[i][i+j], M[i+j][n-i-1], M[n-i-1][n-(i+j)-1]
'''
And now we finish it off:
'''
def solution(n):
    mx = max(max_row(n), max_slash(n))
    rotate_array(arr)
    return max(mx, max_row(n), max_slash(n))

print('Greatest product:', solution(4))    # Greatest product: 70600674





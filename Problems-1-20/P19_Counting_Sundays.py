'''
Problem: How many Sundays fell on the first of the month during the
twentieth century (1 Jan 1901 to 31 Dec 2000)?

To solve a question like this, it's best to stay organized and keep your code
clean. What we need to do is determine which day of the week will fall on the first
of each month. As we all know, days repeat once every seven days, so we will be
taking full advantage of that fact.
First let's create a dictionary of the number of days in a typical (non-leap) year,
sorted by month:
'''
months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
'''
Next we will write a short function to determine if a year is leap. 
If it's divisible by 4 and not divisible by 100 (unless it's divisible by 400),
we have a leap year. 
'''
def is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)
'''
Finally we calculate the number of times the first of the month is a Sunday.
Sunday = 0, Monday = 1, ..., Saturday = 6. We start the count at Tuesday Jan 1 1901
and work our way up by month. All we need to do is add the number of days and take the 
result mod 7 to find the day of the beginning of the next month.  
'''
def how_many(n):
    day, count = 2, 0                    # Initialize day to Tuesday
    for year in range(1901, 2001):
        if is_leap(year):                # Check if leap, then change days to 29 for Feb
            months[2]=29
        for month in range(1, 13):
            if day==0:                   # If Sunday, increase count
                count+=1
            day = (day+months[month])%7  # Add days in the month to day and take it mod 7
        months[2]=28                     # Change back number of days in Feb
    return count

print('Number of Sundays:', how_many(0))    # Number of Sundays: 171

# Write a function that computes the volume of a sphere given its radius.

# The volume of a sphere is given as
# 4/3*π*𝑟3

def vol(rad):
    return 4/3*3.14*rad**3


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low, high+1):
        return "number {} is in range ({},{})".format(num,low,high)
    else:
        print('The number is outside the range.')

# If you only wanted to return a boolean:
def ran_bool(num,low,high):
    return num in range(low, high+1)

Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

def up_low(s):
    low = 0
    up = 0
    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
    
    print('Sample String: '+ s)
    print("No. of Upper case characters :" + str(up))
    print("No. of Lower case characters :" + str(low))

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    return list(set(lst))

# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):
    m = 1
    for i in numbers:
        m =  m * i
    return m

#  Write a Python function that checks whether a passed in string is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(s):
    return s[:] == s[::-1]
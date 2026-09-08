# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

'''
Sources used to complete this assignment include pythontutorial.net for basic syntax reivew, as well as Google Gemini 3.1 pro
to assist with syntax review & understanding. Gemini 3.1 pro also assisted in understanding for what a fibionacci sequence is.
Pythontutorial.net was used for understanding of the numpy library and the numpy.std function for finding the standard deviation of numbers in a list
'''

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
XXX Get input N value from the user - establishes the number of fibonacci numbers to sum
    Set num1 = 0 - first number in the fibonacci sequence
    Set num 2 = 1 - second number in the fibonacci sequence
    Set total_sum = 0 - variable to hold the sum of the fibonacci numbers
    
    Loop N times:
    Add num1 to total_sum - adds the current fibonacci number to the total sum
    Calculate next_sum = num1 + num2 - calculates the next fibonacci number
    Set num1 = num2 - updates num1 to the next number in the sequence
    Set num2 = next_sum - updates num2 to the next number in the sequence

    Output total_sum - prints the final sum of the first N fibonacci numbers
"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 # establishes the number of fibonacci numbers to sum

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # provides a counter to keep track of how many fibonacci numbers have been summed
total = 0 # provides a variable to hold the sum of the fibonacci numbers

while count < N: # loop until we have summed N fibonacci numbers
    total = total + a # add the current fibonacci number (a) to the total sum

    next_value = a + b # calculate the next fibonacci number by adding the previous two numbers (a and b)
    a = b # update a to the current fibonacci number (b) for the next iteration
    b = next_value # update b to the next fibonacci number for the next iteration

    count = count + 1 # increment the counter to keep track of how many fibonacci numbers have been summed

print(total) # print the final sum of the first N fibonacci numbers

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

import numpy
n = 10 # establishes the number of fibonacci numbers to use
fib_sequence = [] # empty list to hold the fibonacci numbers
num1 = 0 # set num1 to the first fibonacci number
num2 = 1 # set num2 to the second fibionacci number
for i in range (n): # loop n times
    fib_sequence.append(num1) # adds the current fibionacci number to the list
    next_value = num1 + num2 # calculates the next fibonacci number
    num1 = num2 # updates num1 to the current fibonacci number for the next iteration
    num2 = next_value # updates num2 to the next fibonacci number for the next iteration

std_dev = numpy.std(fib_sequence) # calculates the standard deviation of the fibonacci sequence using numpy
print("The standard deviation of the first 10 numbers in the fibonacci sequence is: ", std_dev) # prints the calculated standard deviation


# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

N = [5, 10, 15, 20, 25, 30] # establishes a list of N values to calculate the sum of the first N fibonacci numbers

def sum_fib(N): # defines a function that takes an integer N as input
    a = 0 # set a to the first fibonacci number
    b = 1 # set b to the second fibonacci number
    total = 0 # provides a variable to hold the sum of the fibonacci numbers

    for i in range(N): # loop N times
        total += a # add the current fibonacci number (a) to the total sum
        next_value = a + b # calculate the next fibonacci number by adding the previous two numbers (a and b)
        a = b # update a to the current fibonacci number (b) for the next iteration
        b = next_value # update b to the next fibonacci number for the next iteration

    return total # return the final sum of the first N fibonacci numbers

sums = [sum_fib(n) for n in N]
print("The sums of the first N fibonacci numbers are: ", sums)

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0
    b = 1
# a and b were changed from "0" and "1" to 0 and 1 to fix the TypeError. The original code had a and b as strings, which caused a type error when trying to compare them to the integer limit
    index = 1 # This line assigns the variable "index" to 1, which is necessary to avoid the UnboundLocalError that occurs when "index" is used before it is defined

    while a <= limit: # This line causes a type error because a and b are strings, not integers. They need to be converted to integers before comparison
        next_value = a + b
        a = b
        b = next_value
        index += 1

    return index


result = find_fib_above_limit(50) # This line causes a UnboundLocalError because the variable "index" is not defined before it is used in the while loop
print("The index of the first number above your limit is: ", result)

# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_odd_fib(limit): # function renamed from sum_even_fib to sum_odd_fib to reflect what it is now doing (summing odd instead of even)
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 != 0:  # This line was changed from checking if a number is even to if it is odd
            total += b
        a, b = b, a + b
    return total 

print(sum_odd_fib(10)) 

# Add your test cases here

# initially got 2,10,10 respectively before fixing the bug in the code

print("when limit = 5, expecting 10. Got:", sum_odd_fib(5))
print("when limit = 10, expecting 10. Got:", sum_odd_fib(10))
print("when limit = 21, expecting 44. Got:", sum_odd_fib(21))

# %%

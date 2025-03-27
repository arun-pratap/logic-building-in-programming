"""
Write a program that gets one input, a number. The input number indicates how many times to execute the below function. 

Create a function that calculates the sum of all of the numbers between 1 and 10000 (including) and prints it, name the function however you like.

Note! In your code, write the function before it's call statements.
"""


def calculate_sum():
    sum = 0
    for num in range(1, 10001):
        sum += num
    print(sum)


n = int(input())
for n in range(n):
    calculate_sum()
    

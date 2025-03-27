"""
Write a program that gets a dynamic number of input values.

The first input is a number that represents the number of the input values following it. The next input values are whole numbers.

In the end, print the sum of all the input numbers (not including the first input).

 

For example,

Input:

3
1
5
6
Expected output: 12

Explanation:

 1 + 5 + 6 = 12, and there are exactly 3 numbers following the first input number (3).
"""
# first approach

n =  int(input())
total =  0

for num in range(1, n + 1):
    temp = int(input())
    total += temp

print(total)

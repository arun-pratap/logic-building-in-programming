"""
Write a program that receives a list of numbers as input (given),
and prints a list of the indices of the numbers that are either below 50 or they are divisible by 5. 
"""

lst = list(map(int, input().split(",")))
# Write your code below

res  = []
for i in range(len(lst)):
    if (lst[i] < 50 or lst[i] % 5 == 0):
        res.append(i)

print(res)

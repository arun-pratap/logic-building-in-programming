"""
Create a program that receives a list as input (given),
and prints a new list containing only the words longer than 5 characters
"""

lst = input().split(",")
# Write your code below
res = []
for l in lst:
    if(len(l) > 5):
        res.append(l)
print(res)

"""
Write a function named reverse which gets a list of numbers as argument and returns the reversed list.

For example, for [1, 2, 3], the expected output is [3, 2, 1].

Don't use the reverse list builtin function!
"""

def reverse(lst):
    res = []
    for i in range(len(lst) - 1, -1, -1):
        res.append(lst[i])
    return res

# Output
print(reverse([1, 2,3]))

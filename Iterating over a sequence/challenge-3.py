"""
Create a program that receives a string as input,
and it prints how many times the character p is in the string.

Some chars might be uppercase, use char.lower() to convert it to lowercase.
"""

text = input()
# Write your code below
char_count = 0

for i in range(len(text)):
    if text[i].lower() == "p":
        char_count += 1

print(char_count)

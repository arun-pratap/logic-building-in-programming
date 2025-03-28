print("Welcome to FizzBuzz!")

def fizzbuzz(n):
    if  n % 3 == 0 and n % 7 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 7 == 0:
        return "Buzz"
    return str(n)

print(fizzbuzz(int(input())))

"""
Looping The Numbers
Everything is ready, let's play the game!

Challenge:
Loop over the numbers from 1 to the number that the user entered, and each time use the function you created to calculate the FizzBuzz result and output it.
For example, for input of 7 output:
Welcome to FizzBuzz!
1
2
Fizz
4
5
Fizz
Buzz
"""

print("Welcome to FizzBuzz!")

def fizzbuzz(n):
    if  n % 3 == 0 and n % 7 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 7 == 0:
        return "Buzz"
    return str(n)

no = int(input())
for no in range(1, no+1):
    print(fizzbuzz(no))


# print(fizzbuzz(int(input())))

"""
Adding The Twist
================

Challenge
Add a small twist to the game:
Numbers that contain the digit "3" but aren't divisible by 3 or 7 will output Almost Fizz
To check if a string contains a char use in for instance, "a" in word
"""

print("Welcome to FizzBuzz!")

def fizzbuzz(n):
    if  n % 3 == 0 and n % 7 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 7 == 0:
        return "Buzz"
    else:
        if "3" in str(3):
            return "Almost Fizz"
        return str(n)

no = int(input())
for no in range(1, no+1):
    print(fizzbuzz(no))


# print(fizzbuzz(int(input())))

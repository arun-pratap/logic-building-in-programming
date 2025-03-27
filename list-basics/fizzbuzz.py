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

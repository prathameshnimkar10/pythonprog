def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input('Enter a number to find is factorial : '))
print('Factorial is :', factorial(n))
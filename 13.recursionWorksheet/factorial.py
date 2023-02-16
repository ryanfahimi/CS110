def factorial(n):
    if n < 0:
        n = -1
    if n == 0 or n == 1:
        n = 1
    else:
        n *= factorial(n - 1)
    return n


print(factorial(4))

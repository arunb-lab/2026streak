#recursive function to calculate nth Fibonacci number, 
# where each number is the sum of the two preceding ones, starting from 0 and 1.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
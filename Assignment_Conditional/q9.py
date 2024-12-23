# 9. Write a Python program to get the Fibonacci series between 0 to 50.   
# Note : The Fibonacci Sequence is the series of numbers :  
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....  

def fibonacci_series(n):
    fib_series = [0,1]
    while fib_series[-1] + fib_series[-2] <= n:
        fib_series.append(fib_series[-1]+fib_series[-2])
    return fib_series

fib_series = fibonacci_series(50)
print("Fibonacci Series between 0 and 50:")
for num in fib_series:
    print(num, end=" ")

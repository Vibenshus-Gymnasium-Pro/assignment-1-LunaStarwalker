#Fibonacci Sequence

def fibonacciSeries(n):
    if n == 0:
        print("Please enter a higher value.")
    if n == 1:
        return n
    elif n == 2:
        return n
    if n > 2:
        return fibonacciSeries(n-1) + fibonacciSeries(n-2)

num = int(input("Please input a number for your series length: "))

for i in range(1, num):
    print(fibonacciSeries(i), end=" ")


#Fibonacci Series

def fibonacciSeries(n):
    series_Len = n
    n1, n2 = 0, 1
    count = 0

    while count < series_Len:
        print(n1, end = " ")

        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1


num = int(input("Please input a number for your series length: "))
fibonacciSeries(num)


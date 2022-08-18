#Basic Exercise 13

for x in range(1, 11):
    print(x, end="  ")

    for num in range(1, 11):
        product = x*num
        print(product, end=" ")
    print('\n')

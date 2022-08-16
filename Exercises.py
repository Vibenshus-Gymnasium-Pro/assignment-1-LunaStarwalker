#Basic exercise 1

import random

num1 = random.randint(10, 50)
num2 = random.randint(10, 50)

product = num1*num2
numsum = num1+num2

if product<=1000:
    print(product)
else:
    print(numsum)

#Basic Exercise 2
ran = 10

print("Printing current and previous number sum in range " + str(ran))
for x in range(0, ran):
    prenum = x - 1
    thesum = 2*x - 1
    if x == 0:
        print("Current Number: ", x, " Previous Number ", x, " Sum: ", x)
    else:
        print("Current Number: ", x, " Previous Number ", prenum, " Sum: ", thesum)

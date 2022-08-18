#Python Crash Course, exercise 5-11

#creating the list of numbers
num_list = [num for num in range(1, 10)]

#printing the list with proper ordinal
for x in num_list:
    if x == 1:
        print(str(x) + "st")
    elif x == 2:
        print(str(x) + "nd")
    elif x == 3:
        print(str(x) + "rd")
    else:
        print(str(x) + "th")

#Basic Exercise 5

def compare_nums(list):
    print("Given numbers are: ", list)
    if list[0] == list[-1]:
        return True
    else:
        return False


nums = [10, 20, 30, 40, 10]

print("The result is ", compare_nums(nums))


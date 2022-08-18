#Basic Exercise 10

def list_switch(list1, list2):

    new_list = list("")

    for x in list1:
        if x % 2 != 0:
            new_list.append(x)

    for x in list2:
        if x % 2 == 0:
            new_list.append(x)

    return new_list


list_1 = [10, 19, 25, 70, 96]
list_2 = [30, 49, 69, 85, 92]

print(list_switch(list_1, list_2))

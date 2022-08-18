#Python Crash Course, exercise 4-8

#creating the list
new_list = list("")

#appending the cubes of the integers between 1 and 10
for x in range(1, 11):
    cube = x**3
    new_list.append(cube)

#printing the values
for x in new_list:
    print(x)

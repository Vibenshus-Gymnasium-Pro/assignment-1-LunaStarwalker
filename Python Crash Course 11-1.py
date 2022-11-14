#Python Crash Course, exercise 11-1

def city_function(city, country):
    cit = city.title()
    coun = country.title()

    pair = cit + ", " + coun
    return pair


my_city = input("Type the city: ")
my_country = input("Type the country: ")

formatted = city_function(my_city, my_country)
print(formatted)

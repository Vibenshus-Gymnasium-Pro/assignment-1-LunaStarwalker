#Python Crash Course, exercise 11-1

def city_function(city, country, population=0):
    cit = city.title()
    coun = country.title()
    pop = population

    if pop > 0:
        form = cit + ", " + coun + " - population " + str(pop)
    else:
        form = cit + ", " + coun

    return form

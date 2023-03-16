# 2018 Football World Cup Challenge -  www.101computing.net/2018-world-cup-goals-analysis/
import time
import numpy as np
import pandas as pd

countries = np.array([])
players = np.array([])
mints = np.array([])

path = "C:/Users/Donap/Desktop/goals.txt"

def setup():
    print("*********************************************")
    print("*                                           *")
    print("*      2018 World Cup: Goals Analysis       *")
    print("*                                           *")
    print("*********************************************")
    print("")
    print("> Select an option:")
    print("       > A: Total number of goals scored by a given country")
    print("       > B: Total number of goals scored by a given player")
    print("       > C: List the name of all the players who scored for a given country")
    print("       > D: Total number of goals by all countries")
    print("       > E: Total number of goals scored during the first half (45 minutes)")
    print("       > F: Total number of goals scored during the second half (45 minutes to 90 minutes)")
    print("       > G: Total number of goals scored during extra time (after 90 minutes of play)")
    print("       > H: List the names of all the players in the tournament")
    print("       > I: List all of the countries in the tournament")
    print("       > X: Exit")
    print("")

    goaldata = pd.read_csv(path, sep= ";", names=['player','country','time'],usecols=[0,1,2])
    print(goaldata.head())

    for line in goaldata:
        data = line.split(";")

        np.append(countries, data[1])
        np.append(players, data[0])
        np.append(mints, int(data[2]))



# A Procedure to count the number of goals scored by a given country during the 2018 world cup
def goalsPerCountry():
    userInput = input("> Enter country: ").title()
    try:
        goals = np.count_nonzero(countries == userInput)
    except:
        goals = 0
    print("\n> " + userInput + " scored " + str(goals) + " goal(s) in the 2018 world cup.")


def playersPerCountry():
    import numpy as np
    import pandas as pd
    userInput = input("> Enter country:").title()
    goaldata = pd.read_csv("goals.txt")


def allPlayers():
    this_players = np.unique(players)
    print("\n> List of all the players in the tournament:")
    print(*this_players, sep= "\n")

def allCountries():
    this_countries = np.unique(countries)
    print("\n> List of all the countries in the tournament:")
    print(*this_countries, sep="\n")



##################### Main Program Starts Here ##############################
userChoice = ""
while userChoice != "X":
    setup()
    userChoice = input("> Select an option from the menu (A to G) or X to exit: ").upper()

    match userChoice:

        case "A": goalsPerCountry()

        case "B": playersPerCountry()

        case "H": allPlayers()

        case "I": allCountries()

    time.sleep(3)
    print("\n\n\n")
print("Good bye!")
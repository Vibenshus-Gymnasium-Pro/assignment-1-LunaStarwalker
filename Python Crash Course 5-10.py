#Python Crash Course, exercise 5-10

#making the list of current usernames
current_users = ["Annabeth", "Percy", "Grover", "Nico", "Leo", "Rachel"]

#making the list of new usernames
new_users = ["Luke", "PERCY", "Hades", "Hazel", "Nico", "TITAN", "RACheL"]

#looping through usernames with case-insensitivity
for x in new_users:
    for i in current_users:
        if x.casefold() == i.casefold():
            #prining errormessage
            print("The username", x, "is taken. Please choose another username.")

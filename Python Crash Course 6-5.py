#Python Crash Course, exercise 6-5

major_rivers = {
    'nile': 'egypt',
    'thames': 'england',
    'volga': 'russia',
}

for river in major_rivers.keys():
    print("The", river.title(), "runs through", major_rivers[river].title())

print("\nThe rivers are:")
for river in major_rivers.keys():
    print(river.title())

print("\nThe countries are:")
for country in major_rivers.values():
    print(country.title())

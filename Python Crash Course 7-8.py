#Python Crash Course, exercise 7-8

sandwich_orders = ['BMT', 'Italian Meatballs', 'Taco Tuesday', 'Vegan Wonder']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your", current_sandwich, "sandwich")
    finished_sandwiches.append(current_sandwich)

print("\nToday, I made these sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
#Python Crash Course, exercise 7-4

topp = ""
toppings = []

while topp != 'quit':
    topp = input("Type your topping of choice. (Or type 'quit' to stop typing): ")
    if topp != 'quit':
        toppings.append(topp)
        print("\nWe will add", topp, "to your pizza.\n")

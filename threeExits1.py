# Defining variables
topping = (" ")
pizza = []
# Creating the while loop
print("Please use this program to choose the toppings for your pizza.")
print('Enter "Quit" when you are finished.')
active = True
while active:
    topping = input("Enter topping: ")
    if topping.title() == "Quit":
        print("Your pizza toppings are as follows: ")
        for pizzaTopping in pizza:
            print(f"\t {pizzaTopping.title()}")
        active = False
    else:
            print(f"Adding {topping} to your pizza.")
            pizza.append(topping)
        
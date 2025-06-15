"""
Write a loop that prompts the user to enter a series
of pizza toppings until they enter a 'quit' value. As 
they enter each topping, print a message saying you'll 
that topping to their pizza.
"""

while True:
    toppings = input("\nWhat pizza toppings would you like to add? "
        "\nType 'quit' to quit the program. ")
    if toppings.lower() == "quit":
        break
    else:
        print(f"\n{toppings.capitalize()} has been added to the pizza!")
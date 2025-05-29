"""
Start with your program from pizzas.py. Make a copy of the list
of pizzas, and call it friend_pizzas. Then do the following:

    - add a new pizza to the original list.
    - add a different pizza to the list of friend_pizzas.
    - prove that you have two separate lists. 
        - Print the message,'My favorite pizzas are:', 
        and then use a for loop to print the first list. 
        - Print the message, 'My friend's favorite pizzas are:',
        and then use a for loop to print the second list.
        - Make sure each new pizza is stored in the appropriate list.
"""

favorite_pizzas = ['pepperoni', 'combo', 'pesto cheese', 'buffalo chicken',
                   'deep dish', 'supreme', 'thin crust']
friends_favorite_pizza = favorite_pizzas[:]

favorite_pizzas.append('sicilian')
friends_favorite_pizza.append('new york')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("\t-", pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friends_favorite_pizza:
    print("\t-", pizza.title())



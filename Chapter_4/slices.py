"""
Using one of the programs that was written in this chapter,
add several lines to the end of the program that will do the
following:

    - print the message, 'The first three items in the list are:'.
    Then use a slice to print the first three items from that 
    program's list.

    - print the message, 'Three items from the middle of the list are:'.
    Use a slice to print three items from the middle of the list.

    - print the message, 'The last three items in the list are:'. Use
    a slice to print the last three items in the list.
"""

favorite_pizzas = ['pepperoni', 'combo', 'pesto cheese', 'buffalo chicken',
                   'deep dish', 'supreme', 'thin crust', 'meat lovers', 'hawaiian']

for pizza in favorite_pizzas:
    print("My favorite pizza is definetely a " + pizza.title() + " pizza with a side of ranch!")

print("-"*175)
print("The first three items in the list are: ")
for pizza in favorite_pizzas[:3]:
    print(pizza.title())

print("\nThree items from the middle of the list are: ") 
for pizza in favorite_pizzas[3:6]:
    print(pizza.title())

print("\nThe last three items in the list are: ")
for pizza in favorite_pizzas[-3:]:
    print(pizza.title())

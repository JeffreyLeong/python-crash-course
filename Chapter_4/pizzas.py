"""
Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of 
each pizza.

- Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza, you should
have one line of output containing a simple statement like 'I like pepperoni
pizza'.

- add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as,
'I really love pizza!'
"""

favorite_pizzas = ['pepperoni', 'combo', 'pesto cheese', 'buffalo chicken',
                   'deep dish', 'supreme', 'thin crust']

for pizza in favorite_pizzas:
    print("My favorite pizza is definetely a " + pizza.title() + " pizza with a side of ranch!")

print("\nI always have some chicken wings to eat with my pizza.")
print("If not, I'll have pasta. I like pasta too.")
print("Pizza is the perfect food and it hits all the categories of the food pyramid.")
print("Man, I really love me some pizza!")
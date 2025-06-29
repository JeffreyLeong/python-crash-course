"""
Using the list sandwich_orders from deli.py, make sure
the sandwich 'pastrami' appears in the list at least three
times. Add code near the beginning of your program to print
a message saying the deli has run out of pastrami, and then 
use a while loop to remove all occurrences of 'pastrami' 
from sandwich_orders. Make sure no pastrami sandwiches 
end up in finished_sandwiches.
"""
sandwich_orders = ['turkey', 'ham and cheese', 'pastrami',
                   'bacon lettuce tomato', 'pastrami','roast beef',
                   'fried chicken', 'ice cream', 'pastrami',]

finished_sandwiches = []

print("*** Special Announcement ***: \nThe Deli is out of pastrami\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"The {sandwich.title()} sandwich has been made!")
    finished_sandwiches.append(sandwich)

print(f"\nPlease pick up your sandwiches:")
for sando in finished_sandwiches:
    print(f"\t- {sando.title()} sandwich")
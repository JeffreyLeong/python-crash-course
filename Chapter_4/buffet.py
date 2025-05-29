"""
A buffet style restaurant offers only eight basic foods. Think of 
five simple foods, and store them in a tuple.

    - use a for loop to print each food the restaurant offers
    - try to modify one of the items, and make sure that Python
    rejects the change.
    - the restaurant changes its menu, replacing two of the items 
    with different foods. Add a block of code that rewrites the tuple,
    and then use a for loop to print each of the items on the revised
    menu.
"""

buffet_foods = ("macaroni and cheese", "fried rice", "pizza",
                "chicken alfredo", "ice cream", "salad mix",
                "steak", "sushi")

print("Buffet food selection:")
for food in buffet_foods:
    print("\t-", food.title())

print("\nTrying to replace Sushi with Lasagna to the buffet menu: ")
try:
    buffet_foods[-1] = 'lasagna'
except TypeError:
    for food in buffet_foods:
        print("\t-", food.title())
    print("Sorry no Lasagna. Tuples are immutable!")

new_buffet_foods = ("green beans", "baked potato", "spaghetti", "crab legs",
                    "fried chicken", "enchiladas", "cajun shrimp", "corn")

print("\nNew buffet food selection:")
for food in new_buffet_foods:
    print("\t-", food.title())

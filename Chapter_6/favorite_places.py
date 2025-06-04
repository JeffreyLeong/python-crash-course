"""
Make a dictionary called favorite_places. Think of three names 
to use as keys in the dictionary, and store one of three 
favorite places for each person. To make this exercise a bit more
interesting, ask some friends to name a few of their favorite places.
Loop through the dictionary, and print each person's name and their 
favorite place.
"""

favorite_places = {
    "taco": ['seoul', 'auckland', 'sydney'],
    "grant": ['jacksonville', 'tampa', 'fort lauderdale'],
    "nico": ['dallas', 'houston', 'san antonio'],
}

for name, cities in favorite_places.items():
    print(f"\n{name.title()}'s favorite cities are: ")
    for city in cities:
        print(f"\t- {city.title()}")


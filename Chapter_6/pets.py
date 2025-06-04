"""
Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the
owner's name. Store these dictionaries in a list called pets. Next,
loop through your list and as you do print everything you know about 
each pet.
"""

dante = {
    "animal_kind": "dog",
    "owner_name": "jeffrey",
}

moxxy = {
    "animal_kind": "dog",
    "owner_name": "neri",
}

taco = {
    "animal_kind": "bird",
    "owner_name": "tooms",
}

smokey = {
    "animal_kind": "cat",
    "owner_name": "julie",
}

pets = [dante, moxxy, taco, smokey]

for info in pets:
    print(f"\nType of Animal: {info['animal_kind'].title()}")
    print(f"Owner's Name: {info['owner_name'].title()}")
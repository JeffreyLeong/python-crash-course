"""
Start with a copy of magicians.py. Write a function called make_great() 
that modifies the list of magicians by adding the phrase 'the Great' to
each magician's name.  Call show_magicians() to see that the list has
actually been modified.
"""
def show_magicians(magician_names):
    for name in magician_names:
        print(name)

def transfer_magician(magician_names, great_magicians):
    """Transfer magician's name from one list to another list for editing purposes"""
    while magician_names:
        current_name = magician_names.pop()
        great_magicians.append(current_name)

def make_great(names):
    """Modify each magician's name to have 'The Great' in front of each name"""
    for i in range(len(names)):
        names[i] = f"The Great {names[i]}"
        
magician_names = ["HunterxHunter", "Lucky Number Slevin", "Average Joe"]
great_magicians = []

transfer_magician(magician_names, great_magicians)
make_great(great_magicians)
show_magicians(great_magicians)
print()
show_magicians(magician_names)




# def show_magicians(magician_names):
#     """Print the name of each magician"""
#     for name in magician_names:
#         print(name)

# def make_great(magician_names):
#     """Modify each magician's name to have 'The Great' in front of each name"""
#     for name in range(len(magician_names)):
#         magician_names[name] = f"The Great {magician_names[name]}"
        
# magician_names = ["HunterxHunter", "Lucky Number Slevin", "Average Joe"]

# make_great(magician_names)
# show_magicians(magician_names)


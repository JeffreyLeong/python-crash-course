"""
Start with your work from great_magicians.py. Call the 
function make_great() with a copy of the list of magician's
names. Because the original list will be unchanged, return 
the new list and store it in a separate list. Call 
show_magicians() with each list to show that you have one
list of the original names and one list with 'the Great' 
added to each magician's name.
"""
def show_magicians(magician_names):
    for name in magician_names:
        print(name)

def make_great(names):
    """Modify each magician's name to have 'The Great' in front of each name"""
    new_list = []
    for name in names:
        new_list.append(f"The Great {name}")
    return new_list
        
magician_names = ["HunterxHunter", "Lucky Number Slevin", "Average Joe"]
great_magicians = make_great(magician_names[:]) # pass a copy to avoid changing

print("Original Magicians: ")
show_magicians(magician_names)
print("\nGreat Magicians:")
show_magicians(great_magicians)


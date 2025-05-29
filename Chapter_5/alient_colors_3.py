"""
Turn your if-else chain from alien_colors_2.py into 
an if-elif-else chain.

- if the alien is green, print a message that the 
player earned 5 points.

- if the alien is yellow, print a message that the 
player earned 10 points.

- if the alien is red, print a message that the
player earned 15 points.

- write three verions of this program, making sure
each message is printed for the appropriate color alien.
"""
print("------ Version 1 ------")
alien_color_1 = "green"

if alien_color_1 == "green":
    print("Player earned 5 points.")
elif alien_color_1 == "yellow":
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")

print("\n------ Version 2 ------")

alien_color_2 = "red"

if alien_color_2 == "green":
    print("Player earned 5 points.")
elif alien_color_2 == "yellow":
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")

print("\n------ Version 3 ------")

alien_color_3 = "yellow"

if alien_color_3 == "green":
    print("Player earned 5 points.")
elif alien_color_3 == "yellow":
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")
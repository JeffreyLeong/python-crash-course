"""
Choose a color for an alien as you did in alien_colors_1.py, 
and write an if-else chain.

- If the alien's color is green, print a statement that the 
player just earend 5 points for shooting the alien.

- If the alien's color isn't green, print a statement that the 
player just earned 10 points.

- Write one version of this program that runs the if block and another
that runs the else block.
"""


alien_color_1 = "green"

print("------ Version 1 ------")
if alien_color_1 == "green":
    print("Player just earned 5 points.")
else:
    print("Player just earned 10 points.")

alien_color_2 = "red"
print("\n------ Version 2 ------")
if alien_color_2 == "green":
    print("Player just earned 5 points")
else:
    print("Player just earned 10 points.")


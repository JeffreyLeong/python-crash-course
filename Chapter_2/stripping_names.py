"""
Store a person's name, and include some whitepace characters
at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.

Print the name once, so the whitespace around the name is
displayed. Then print the name using each of the three
stripping functions, lstrip(), rstrip(), and strip()
"""

name= "\t\n  Charlie Brown   \n\t"

print("Original with whitespace")
print(name)

print("\nleft strip")
print(name.lstrip())

print("\nright strip")
print(name.rstrip())

print("\nstrip all")
print(name.strip())
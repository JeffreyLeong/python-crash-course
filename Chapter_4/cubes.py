"""
A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the 
first 10 cubes (that is, the cube of each integer from 1 through 10),
and use a for loop to print out the value of each cube.
"""
cubes = list(range(1,11))

for cube in cubes:
    number_cubed = cube ** 3
    print(number_cubed) # prints the value, not the list
print(cubes) # prints a list 
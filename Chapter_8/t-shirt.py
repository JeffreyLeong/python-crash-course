"""
Write a function called make_shirt() that accepts a size and 
the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of
the shirt and the message printed on it.

Call the function once using positional arguments to make a
shirt. Call the function a second time using keyword arguments.
"""

def make_shirt(size, text):
    """Display information about a shirt"""
    print(f"I have a {size} shirt and it says:\n{text}!")

print("-----Positional Arguments: ")
make_shirt("small", "Drive for show, putt for dough")

print("\n-----Key word arguments: ")
make_shirt(size="medium", text="Even my divots are straight")

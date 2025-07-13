"""
Modify the make_shirt() function so that shirts are large
by default with a message that reads 'I love Python'. Make a 
large shirt and a medium shirt with the default message, and 
a shirt of any size with a different message.
"""
def make_shirt(size="large", text="I love Python"):
    """Display information about a shirt"""
    print(f"I have a {size} shirt and it says:\n{text}!")

make_shirt("medium")
make_shirt("small", "Hand down, man down")


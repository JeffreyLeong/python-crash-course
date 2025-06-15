"""
Write a program that asks the user how many people
are in their dinner group. If the answer is more than
eight, print a message saying they'll have to wait for 
a table. Otherwise, report that their table is ready.
"""

question = int(input("How many people are in your dinner group?: "))

if question > 8:
    print("Sorry, there will be a wait for your table.")
else:
    print("Your table is ready.")
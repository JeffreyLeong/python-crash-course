"""
Write a program that polls users about their dream
vacation. Write a prompt similar to "If you could 
visit one place in the world, where would you go?"
Include a block of code that prints to results of 
the poll
"""

responses = {}

while True:
    name = input("\nWhat is your name?: ")
    destination = input("\nIf you could visit one place in the world," \
    " where would you go?: ")

    responses[name] = destination

    repeat = input("\nWould you like to try again?(yes/no): ")
    if repeat.lower() == "no":
        break

print("\n--- Polling Results ---")
for name, destination in responses.items():
    print(f"{name.capitalize()} would like to visit {destination.title()}!")


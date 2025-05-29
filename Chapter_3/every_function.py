"""
Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities,
languages, or anything else you'd like. Write a program that 
creates a list containing these items and then uses each function 
introduced in this chapter at least once.
"""

import random

activities = ["basketball", "tennis", "golf", "football",
          "hockey", "billiards", "reading", "coding", "learning",
          "sleeping", "eating", "working out"]

# prints every "even numbered" other activity
print("activities at even index positions:")
for index in range(len(activities)):
    if index % 2 == 0:
        print(activities[index])
print("-"*175)

# prints every "odd numbered" other activity
print("activities at odd index positions:")
for index in range(len(activities)):
    if index % 2 == 1:
        print(activities[index])
print("-"*175)

# prints a statement with the "activity"
choice = random.choice(activities)
print(f"I think {choice} is my favorite activity!")
print("-"*175)

# demonstrate append
print("we added 'cooking' to the end of the list: ")
activities.append("cooking")
print(activities)
print("-"*175)

# demonstrate insert
activities.insert(4, "toilet")
print("new activity added at position 5: " + activities[4])
print(activities)
print("-"*175)

# demonstrate pop
popped_activity = activities.pop()
print(f"popped last activity: {popped_activity}")
print(activities)
print("-"*175)

# demonstrate remove
print("we removed an 'activity' that is not an activity (toilet): ")
activities.remove("toilet")
print(activities)
print("-"*175)

# demonstrate del
del activities[8]
print("this is what the list looks like when 9th entry, learning, is not there: ")
print(activities)
print("-"*175)

# prints list in alphabetical order via sort(), permanent alphabetical
activities.sort()
print("list sorted alphabetically, permanently: ")
print(activities)
print("-"*175)

# prints list in reverse alphabetical order via sort(), permanent reverse alphabetical
activities.sort(reverse=True)
print("list sorted reverse alphabetically, permanently: ")
print(activities)
print("-"*175)

# prints list in alphabetical order via sorted(), temporary sort
print("temporarily sorted alphabetically: ")
print(sorted(activities))
print("\noriginal sort before the temporary sort: ")
print(activities)
print("-"*175)

# prints list in reverse via reverse()
print("reverse order of the current list is: ")
activities.reverse()
print(activities)
print("-"*175)

# demonstrate len()
print("This list has " + str(len(activities)) + " entries.")
print("-"*175)
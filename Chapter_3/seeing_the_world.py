"""
Think of at least five places in the world you'd like to visit.

- Store the locations in a list. Make sure the list is not in alphabetical order.
- Task 1: Print your list in its original order. Don't worry about printing the list neatly,
just print it as a raw Python list.
- Task 2: use sorted() to print your list in alphabetical order without modifying the actual
list.
- Task 3: show that your list is still in its original order by printing it.
- Task 4: use sorted() to print your list in reverse alphabetical order without changing the 
order of the original list.
- Task 5: show that your list is still in its original order by printing it again.
- Task 6: use reverse() to change the order of your list. Print the list to show
that its order has changed.
- Task 7: use reverse() to change the order of your list again. print the list to show
that its order has been changed.
- Task 8: use sort() to change your list so it's stored in reverse alphabetical order.
print the list to show that its order has changed.
"""

places_to_visit = ['Spain', 'Australia', 'Canada', 'Brazil', 'Japan']

print("Task 1: original list order: ")
print(places_to_visit)
print("-"*75)

print("Task 2: alphabetical order with sorted(): ")
sorted_alphabetically = sorted(places_to_visit)
print(sorted_alphabetically)
print("-"*75)

print("Task 3: original list order: ")
print(places_to_visit)
print("-"*75)

print("Task 4: reverse alphabetical order with sorted(): ")
print(sorted(places_to_visit, reverse=True))
print("-"*75)

print("Task 5: present original list: ")
print(places_to_visit)
print("-"*75)

print("Task 6: list with first reverse(): ")
places_to_visit.reverse()
print(places_to_visit)
print("-"*75)

print("Task 7: list with second reverse(): ")
places_to_visit.reverse()
print(places_to_visit)
print("-"*75)

print("Task 8: reverse alphabetical order with sort(): ")
places_to_visit.sort(reverse=True)
print(places_to_visit)

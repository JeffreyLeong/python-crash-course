"""
Start with person.py. Make two new dictionaries representing 
different people, and store all three dictionaries in a list
called people. Loop through your list of people. As you loop
through the list, print everything you know about each person.
"""

my_friend = {
    "first_name": "kevin", 
    "last_name": "james",
    "age": 19,
    "city": "los angeles",
}

my_friend_1= {
        "first_name": "john",
        "last_name": "zelle",
        "age": 49,
        "city": "new york",
    }

my_friend_2 =  {
        "first_name": "travis",
        "last_name": "young",
        "age": 31,
        "city": "atlanta"
    }

people = [my_friend, my_friend_1, my_friend_2,]

for person in people:
    print(f"\nFirst name: {person['first_name'].title()}")
    print(f"Last Name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")
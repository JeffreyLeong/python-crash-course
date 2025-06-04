"""
Modify your program from favorite_numbers.py so each person can
have more than one favorite number. Then print each person's name
along with their favorite numbers.
"""

favorite_numbers = {
    "john": [54, 7, 101, 54],
    "mike": [66, 32, 1, 99, 19],
    "jeff": [5],
    "jd": [12, 95, 44, 63],
    "eman": [13, 7, 4, 666],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are: ")
    for i in numbers:
        print(f"\t- {i}")


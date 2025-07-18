"""
Write a function called city_country() that takes in the
name of a city and its country. The function should return
a string formatted like this:

"Santiago, Chile"

Call your function with at least three city-country pairs,
and print the value of tha's returned.
"""
def city_country(city, country):
    return f"{city}, {country}"

name1 = city_country("San Diego", "USA")
name2 = city_country("Paris", "France")
name3 = city_country("Brussels", "Germany")

print(name1)
print(name2)
print(name3)
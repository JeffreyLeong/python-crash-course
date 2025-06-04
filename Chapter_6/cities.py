"""
Make a dictionary called 'cities'. Use the names of three cities
as keys in your dictionary. Create a dictionary of information about 
city and include the country that the city is in, its approximate 
population, and one fact about that city. The keys for each city's 
dictionary should be something like 'country', 'population', and 
'fact'. Print the name of each city and all the information you
have stored about it.
"""

cities = {
    'memphis': {
        'country': 'united states of america',
        'population': 620000,
        'fact': 'Memphis is home of the blues and the birth place of rock and roll',
    },
    'puerto vallarta': {
        'country': 'mexico',
        'population': 300000,
        'fact': 'Puerto Vallarta has one of the longest and deepest bays in the world',
    },
    'calgary': {
        'country': 'canada',
        'population': 1400000,
        'fact': 'Calgary is one of the sunniest cities in North America',
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")

    country = city_info['country']
    print(f"Country: {country.title()}")

    population = city_info['population']
    print(f"Estimated Population: {population}")

    fact = city_info['fact']
    print(f"Fun Fact: {fact}!")


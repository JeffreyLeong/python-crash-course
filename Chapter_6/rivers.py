"""
Make a dictionary containing three major rivers
and the country each river runs through. One 
key-value pair might be 'nile': 'egypt'.

- use a loop to print a sentence about each river,
such as 'The Nile runs through Egypt.'

- Use a loop to print the name of each river included
in the dictionary.

- Use a loop to print the name of each country included 
in the dictionary.
"""

rivers = {
    "nile": "egypt",
    "mississippi": "united states of america",
    "amazon": "brazil", 
}

for name, country in rivers.items():
    print(f"The {name.title()} River runs through {country.title()}.")
print("-"*80)

for name in rivers:
    print(name.title())
print("-"*80)


for country in rivers.values():
    print(country.title())
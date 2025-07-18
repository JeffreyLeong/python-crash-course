"""
Write a function that stores information about a car in a 
dictionary. The function should always receive a manufacturer
and a model name. It should then accept an arbitrary number
of keyword arguments. Call the function with the required 
information and two other name-value pairs, such as a color or
an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that's returned to make sure all the information was
stored correctly.
"""

def car_info(manufacturer, model_name, **add_ons):
    car = {}
    car["manufacturer"] = manufacturer
    car["model_name"] = model_name
    for key, value in add_ons.items():
        car[key] = value
    return car

car = car_info("Toyota", "4Runner", color="white", trim="Venture 4WD",
          engine="4.0 liter V6", hybrid=False)
print(car)
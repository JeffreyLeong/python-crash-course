"""
Start with your class from restaurant.py. Create
three different instances from the class, and call
describe_restaurant() for each instance.
"""

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant!")

restaurant_1 = Restaurant("Flemmings", "steakhouse")
restaurant_2 = Restaurant("Puesta", "mexican")
restaurant_3 = Restaurant("Santo Market", "poki")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
"""
An ice cream stand is a specific kind of restaurant. Write
a class called 'IceCreamStand' that inherits from the 'Restaurant'
class you wrote in restaurant.py or number_served.py. Either version
of the class will work; just pick the one you like better. Add an attribute
called 'flavors' that stores a list of ice cream flavors. Write a method 
that displays these flavors. Create an instance of 'IceCreamStand', and
call this method.
"""
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant!")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"Our flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor}")

restaurant = IceCreamStand("Baskin Robins", 
                           "ice cream", ['cherry', 'chocolate', 
                            'vanilla', 'butterscotch', 'peanut butter'])
restaurant.describe_restaurant()
restaurant.display_flavors()
"""
Start with your program from restaurant.py. Add an attribute called
number_served with a default value of 0. Create an instanace called
restaurant from this class. Print the number of customers the restaurant
has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and 
print the value again.

Add a method called increment_number_served() that lets you increment the
number of customers who've been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
"""

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is a {self.cuisine_type.title()} restaurant!")
      
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, numbers_served):
        self.number_served += numbers_served

restaurant = Restaurant("flemings", "steakhouse")
print(restaurant.number_served)
restaurant.set_number_served(18)
print(restaurant.number_served)
# print(f"{restaurant.restaurant_name.title()} has served {restaurant.number_served} customers this morning.")
restaurant.increment_number_served(45)
# print(f"{restaurant.restaurant_name.title()} the {restaurant.cuisine_type.title()} ended up serving a total of {restaurant.number_served} customers today!")
print(restaurant.number_served)
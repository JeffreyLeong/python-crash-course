"""
Make a class called User. Create two attributes called 
first_name and last_name, and then create several other
attributes that are typically stored in a user profile. Make
a method called describe_user() that prints a summary of
the user's information. Make another method called greet_user()
that prints a personalized greeting to the user.

Create several instances representing different users, and 
call both methods for each user.
"""

class User():

    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby

    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()} is {self.age} and is really into {self.hobby}.")
    
    def greet_user(self):
        print(f"Hi {self.first_name.title()}. Welcome to the thunder-dome!")
    
user_1 = User("Cole", "trickle", 32, "racing")
user_2 = User("james", "bond", 45, "espionage")
user_3 = User("tom", "brady", 29, "football")
user_4 = User("colin", "morikawa", 33, "golf")

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

user_4.describe_user()
user_4.greet_user()

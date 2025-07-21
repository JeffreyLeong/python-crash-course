"""
Add an attribute called login_attempts to your User class from users.py. 
Write a method called increment_login_attempts() that increments the value 
login_attempts by 1. Write another method called reset_login_attempts() that
resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was 
incremented properly, and then call reset_login_attempts(). Print login_attempts
again to make sure it was reset to 0.
"""

class User():

    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()} is {self.age} and is really into {self.hobby}.")
    
    def greet_user(self):
        print(f"Hi {self.first_name.title()}. Welcome to the thunder-dome!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User("Cole", "trickle", 32, "racing")
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)


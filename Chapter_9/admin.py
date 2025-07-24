"""
An administrator is a special kind of user. Write a class
called 'Admin' that inherits from the 'User' class you wrote 
in users.py or login_attempts.py. Add an attribute, 'privileges',
that stores a list of strings like 'can add post', 'can delete post',
'can ban user', and so on. Write a method called 'show_privileges()' 
that lists the administrator's set of privileges. Create an instance 
'Admin', and call your method.
"""

class User():

    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby

    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()} is {self.age} years old and is really into {self.hobby}.")
    
    def greet_user(self):
        print(f"Hi {self.first_name.title()}. Welcome to the thunder-dome!")

class Admin(User):

    def __init__(self, first_name, last_name, age, hobby, privileges=None):
        super().__init__(first_name, last_name, age, hobby)
        if privileges is None:
            self.privileges = ['Delete posts', 'Add posts', 'Create new user',
                           'Delete users', 'Create new posts', 'Power off system', 
                           'Restart system', 'Power on system']
        else:
            self.privileges = privileges
    
    def show_privileges(self):
        if self.privileges:
            print("\nAdmin Privileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("This admin has no privileges assigned.")

admin_1 = Admin("James", "Bond", 43, "Espionage")
admin_1.show_privileges()
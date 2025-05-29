"""
Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a 
greeting to each user after they log in to a website. 
Loop through a list, and print a greeting to each user:

- If the username is 'admin', print a special greeting,
such as "Hello admin, would you like to see a status report?"

- Otherwise, print a generic greeting, such as "Hello Eric, 
thank you for logging in again."
"""

usernames = ['admin', 'eric', 'jane', 'jello', 'bond', 
             'cake', 'tree']

for user in usernames:
    if user == "admin":
        print(f"Hello {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")


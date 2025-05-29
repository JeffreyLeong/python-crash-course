"""
You just found out that your new dinner table won't arrive in time for
the dinner, and you have space for only two guests.

- start with your program from more_guests.py. Add a new line that print
a message saying that you can invite only two people for dinner.

- use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list,
print a message to that person letting them know you're sorry you can't 
invite them to dinner.

- print a message to each of the two people still on your list, letting them 
know they're still invited.

- use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
"""

dinner_invites = ["Michael Jordan", "Kobe Bryant", "Josh Jacobs",
                "Horatio Caine", "Megan Fox", "Serena Williams",
                "Florence Pugh"]

message_1 = "Hi " + dinner_invites[0] + ", I would like to invite you to dinner."
message_2 = "Hi " + dinner_invites[1] + ", I would like to invite you to dinner."
message_3 = "Hi " + dinner_invites[2] + ", I would like to invite you to dinner."
message_4 = "Hi " + dinner_invites[3] + ", I would like to invite you to dinner."
message_5 = "Hi " + dinner_invites[4] + ", I would like to invite you to dinner."
message_6 = "Hi " + dinner_invites[5] + ", I would like to invite you to dinner."
message_7 = "Hi " + dinner_invites[6] + ", I would like to invite you to dinner."

print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)
print(message_7)

print("-" * 75)

print("Hi everyone unfortunately, " + dinner_invites[3] + " is unable to make dinner. ")

del dinner_invites[3]
dinner_invites.insert(3, "Rachel McAdams")

print("However, " + dinner_invites[3] + " will now attend dinner.")
print("-"*75)

message_1 = "Hi " + dinner_invites[0] + ", I would like to invite you to dinner."
message_2 = "Hi " + dinner_invites[1] + ", I would like to invite you to dinner."
message_3 = "Hi " + dinner_invites[2] + ", I would like to invite you to dinner."
message_4 = "Hi " + dinner_invites[3] + ", I would like to invite you to dinner."
message_5 = "Hi " + dinner_invites[4] + ", I would like to invite you to dinner."
message_6 = "Hi " + dinner_invites[5] + ", I would like to invite you to dinner."
message_7 = "Hi " + dinner_invites[6] + ", I would like to invite you to dinner."

print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)
print(message_7)

print("-"*75)
print("Good News! We have a bigger table.")
print("-"*75)
dinner_invites.insert(0, "Ana De Armas")
dinner_invites.insert(5, "Ashton Jeanty")
dinner_invites.append("Lana Rhodes")

message_1 = "Hi " + dinner_invites[0] + ", I would like to invite you to dinner."
message_2 = "Hi " + dinner_invites[1] + ", I would like to invite you to dinner."
message_3 = "Hi " + dinner_invites[2] + ", I would like to invite you to dinner."
message_4 = "Hi " + dinner_invites[3] + ", I would like to invite you to dinner."
message_5 = "Hi " + dinner_invites[4] + ", I would like to invite you to dinner."
message_6 = "Hi " + dinner_invites[5] + ", I would like to invite you to dinner."
message_7 = "Hi " + dinner_invites[6] + ", I would like to invite you to dinner."
message_8 = "Hi " + dinner_invites[7] + ", I would like to invite you to dinner."
message_9 = "Hi " + dinner_invites[8] + ", I would like to invite you to dinner."
message_10 = "Hi " + dinner_invites[9] + ", I would like to invite you to dinner."

print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)
print(message_7)
print(message_8)
print(message_9)
print(message_10)

print("-"*75)
print("Sorry! The new table is not here yet. We can only have 2 people instead.")
print("-"*75)

first_pop = dinner_invites.pop()
pop_message_1 = "I'm sorry, " + first_pop + ", I can't have you over for dinner."
print(pop_message_1)

second_pop = dinner_invites.pop()
pop_message_2 = "I'm sorry, " + second_pop + ", I can't have you over for dinner."
print(pop_message_2)

third_pop = dinner_invites.pop()
pop_message_3 = "I'm sorry, " + third_pop + ", I can't have you over for dinner."
print(pop_message_3)

fourth_pop = dinner_invites.pop()
pop_message_4 = "I'm sorry, " + fourth_pop + ", I can't have you over for dinner."
print(pop_message_4)

fifth_pop = dinner_invites.pop()
pop_message_5 = "I'm sorry, " + fifth_pop + ", I can't have you over for dinner."
print(pop_message_5)

sixth_pop = dinner_invites.pop()
pop_message_6 = "I'm sorry, " + sixth_pop + ", I can't have you over for dinner."
print(pop_message_6)

seventh_pop = dinner_invites.pop()
pop_message_7 = "I'm sorry, " + seventh_pop + ", I can't have you over for dinner."
print(pop_message_7)

eighth_pop = dinner_invites.pop()
pop_message_8 = "I'm sorry, " + eighth_pop + ", I can't have you over for dinner."
print(pop_message_8)

del dinner_invites[1]
del dinner_invites[0]

print("-"*75)
print(dinner_invites)
print("-"*75)
"""
Working with any of the guest list programs, use len()
to print a message indicatting the number of people 
you are inviting to dinner.
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

print("However, " + dinner_invites[3] + " will now attend dinner.\n")

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
print("\nGood News! We have a bigger table.")
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
print("Tonight, we have " + str(len(dinner_invites)) + " guests attending dinner!") 
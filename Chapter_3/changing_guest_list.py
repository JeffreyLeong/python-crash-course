"""
You just heard that one of your guests can't
make the dinner, so you need to send out a new
set of invitations. You'll have to think of 
someone else to invite.

    - Start with your program from guest_list.py. Add a print
    statement at the end of your program stating the name of the
    guest who can't make it.

    - Modify your list, replacing the name of the guest who can't
    make it with the name of the new person you are inviting.

    - Print a second set of invitation messages, one for each 
    person who is still in your list.
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
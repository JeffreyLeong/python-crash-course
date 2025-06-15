"""
A movie theater charges different ticket prices depending on a 
person's age. If a person is under the age of 3, the ticket is
free; if they are between 3 and 12, the ticket is $10; and if they
are over the age 12, the ticket is $15. Write a loop in which you ask
users their age, and then tell them the cost of their movie ticket.
"""

while True:
    age = input("How old are you? (type 'quit' to end the program): ")

    if age.lower() == 'quit':
        print("Goodbye!")
        break

    try:
        how_old = int(age)

        if how_old < 3:
            print("Ticket is free")
        elif 3 <= how_old <= 12:
            print("Ticket is $10")
        else:
            print("Ticket is $15")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'quit'.")

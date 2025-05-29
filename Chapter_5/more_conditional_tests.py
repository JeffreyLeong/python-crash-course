"""
You don't have to limit the number of tests you create to 10. 
If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False
result for each of the following:

- Tests for equality and inequality with strings
- Tests using the lower() function
- Numerical tests involving equality and inequality,
greater than and less than, greater than or equal to,
and less than or equal to.
- Test using the 'and' keyword and the 'or' keyword.
- Test whether an item is in a list
- Test whether an item is not in a list
"""

names = ['pam', 'malory', 'archer', 'cyril', 'brett',
         'lana', 'ray', 'JusTin', 'ArIana']

# String equality/inequality
print("Is 'pam' == 'pam'? I predict True")
print('pam' == 'pam')

print("\nIs 'pam' != 'archer'? I predict True")
print('pam' != 'archer')

print("\nIs 'pam' == 'Pam'? I predict False")
print('pam' == 'Pam')

# lower() test
print("\nIs 'justin'.lower() in names? I predict True")
print('justin'.lower() in [name.lower() for name in names])

print("\nIs 'ariana'.lower() in names? I predict True")
print('ariana'.lower() in [name.lower() for name in names])

# Numerical tests
age = 30

print("\nIs age == 30? I predict True")
print(age == 30)

print("\nIs age != 25? I predict True")
print(age != 25)

print("\nIs age > 25? I predict True")
print(age > 25)

print("\nIs age < 40? I predict True")
print(age < 40)

print("\nIs age >= 30? I predict True")
print(age >= 30)

print("\nIs age <= 29? I predict False")
print(age <= 29)

# 'and' / 'or' tests
print("\nIs 'pam' in names and 'lana' in names? I predict True")
print('pam' in names and 'lana' in names)

print("\nIs 'pam' in names and 'fez' in names? I predict False")
print('pam' in names and 'fez' in names)

print("\nIs 'pam' in names or 'fez' in names? I predict True")
print('pam' in names or 'fez' in names)

print("\nIs 'kelso' in names or 'donna' in names? I predict False")
print('kelso' in names or 'donna' in names)

# in and not in
print("\nIs 'pam' in names? I predict True")
print('pam' in names)

print("\nIs 'kelso' not in names? I predict True")
print('kelso' not in names)

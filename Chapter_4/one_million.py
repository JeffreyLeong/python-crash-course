"""
Make a list of the numbers from one to one million,
and then use a for loop to print the numbers. (if 
the output is taking too long, stop it by pressing 
crtl-c or by closing the output windows.)
"""

import time
start_time = time.time()

for number in range(1, 1000000):
    print(number)

elapsed_time = time.time() - start_time
print("\nMy program took", round(elapsed_time, 2), "seconds to run")
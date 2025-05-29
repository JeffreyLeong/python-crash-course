"""
Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list 
actually starts at one and ends at one million. Also,
use the sum() function to see how quickly Python can
add a million numbers.
"""
import time

start_time = time.time() 

million_numbers = list(range(1, 1000001))

print("lowest number:", min(million_numbers))
print("highest number:", max(million_numbers))

million_sum = sum(million_numbers)

print("Sum of a million is:", million_sum)
elapsed_time = time.time() - start_time
print("The sum to a million took", round(elapsed_time, 2), "seconds to complete.")
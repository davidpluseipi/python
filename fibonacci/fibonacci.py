# Stop at the next_element number after m
from typing import Any, Union

m = 1000

# Start the Fibonacci sequence
f = [1, 1]

# Loop until you get the first element larger than m
while f[-1] < m:
    next_element = f[-1] + f[-2]
    f.append(next_element)

# Print the resulting sequence
print(f)

# Import Modules
# import numpy as np
# import pandas as pd
# import matplotlib as mp
# import matplotlib.pyplot as plt
# import scipy as sc
# import python_utils as ut

# Stop at the next number after m
m = 1000

# Start the Fibonacci sequence
f = [1, 1]


# Loop until you get the first element larger than m
while f[-1] < m:
    next = f[-1] + f[-2]
    f.append(next)

# Print the resulting sequence
print(f)

# A simple signal

# Import modules
import numpy as np
import matplotlib.pyplot as plt

# The stuff we need for the signal
N = 64                  # number of samples
k = list(range(0, N))   # list of index values of samples
f = 500                 # freq (Hz)
fs = 3*f                # sampling freq
Ts = 1/fs               # sampling period

# Putting it all together
y = np.cos(2 * np.pi * f * np.asarray(k) * Ts)
plt.plot(k, y)
plt.show()


file_obj = open("c:/g/code/python/signal/signal_data.txt", "w")

for i in range(0, N-1):
    file_obj.write(f"{str(y[i])}\n")

file_obj.close()

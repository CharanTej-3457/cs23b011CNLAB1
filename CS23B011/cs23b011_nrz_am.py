import numpy as np
import matplotlib.pyplot as plt

data = [1,0,1,0,1,1,0]
fc = 20
bits_per_sample = 200
nrz_sig = []

for bit in data:

    if bit == 1:
        nrz_sig.extend([1] * bits_per_sample)
    else:
        nrz_sig.extend([-1] * bits_per_sample)

nrz_sig = np.array(nrz_sig)
#commit-1
#print(nrz_sig , nrz_sig.dtype)

t = np.arange(len(nrz_sig)) / fs
carrier_signal = np.sin(2 * np.pi * fc * t)
#commit-2
am_signal = (1+nrz_sig) * carrier_signal
#commit - 3




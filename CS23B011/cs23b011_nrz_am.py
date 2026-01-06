
import numpy as np
import matplotlib.pyplot as plt

data = [1,0,1,0,1,1,0]
fc = 20 # Carrier frequency in Hz
bits_per_sample = 200
fs = 200 # Sampling frequency in Hz

nrz_sig = []

for bit in data:

    if bit == 1:
        nrz_sig.extend([1] * bits_per_sample)
    else:
        nrz_sig.extend([-1] * bits_per_sample)

nrz_sig = np.array(nrz_sig)


t = np.arange(len(nrz_sig)) / fs


carrier_signal = 5*np.sin(2 * np.pi * fc * t)


am_signal = (4+nrz_sig) * carrier_signal


plt.figure(figsize=(12, 8))

# Subplot 1: NRZ Message Signal
plt.subplot(3, 1, 1)
plt.plot(t, nrz_sig, drawstyle='steps-pre')
plt.title("NRZ Message Signal")
plt.ylabel('Amplitude')
plt.grid(True)
plt.yticks([-1, 1])

# Subplot 2: Carrier Signal
plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal)
plt.title("Carrier Signal (20 Hz)")
plt.ylabel('Amplitude')
plt.grid(True)

# Subplot 3: AM Modulated Signal
plt.subplot(3, 1, 3)
plt.plot(t, am_signal)
plt.title("AM Modulated Signal")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.savefig("amplots.pdf")
plt.show()



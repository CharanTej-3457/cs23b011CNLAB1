import numpy as np
from matplotlib.pyplot import pyplot as plt

data = [1,0,1,0,1,1,0]
data_seq = np.array(data)
samples_per_bit = 200
fc = 20
data_seq_bits = np.zeros(len(data_seq) * samples_per_bit)
print(data_seq_bits , data_seq_bits.dtype)


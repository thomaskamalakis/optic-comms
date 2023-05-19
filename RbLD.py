import numpy as np
import matplotlib.pyplot as plt

b2 = 20e-27
Rb = np.linspace(10, 80, 200) * 1e9
T0 = 1/Rb
LD = T0 ** 2 / b2

plt.close('all')
plt.figure()
plt.plot(Rb/1e9, LD/1e3)
plt.ylabel('LD [Km]')
plt.xlabel('Rb [Gb/s]')

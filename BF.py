import numpy as np
import matplotlib.pyplot as plt

b2 = 20e-27
L = np.linspace(1, 100, 200) * 1e3
Rb = 10e9
T0 = 1/Rb

BF = np.sqrt( 1 + (b2 * L / T0 ** 2) ** 2)
broadening = (BF - 1) * 100
plt.close('all')
plt.figure()
plt.plot(L/1e3, broadening, label = 'Rb=10Gb/s')
plt.xlabel('L [Km]')
plt.ylabel('Broadening [%]')

Rb = 40e9
T0 = 1/Rb
BF = np.sqrt( 1 + (b2 * L / T0 ** 2) ** 2)
broadening = (BF - 1) * 100
plt.plot(L/1e3, broadening, label = 'Rb=40Gb/s')
plt.legend()
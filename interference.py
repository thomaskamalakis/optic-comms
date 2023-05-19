import numpy as np
import matplotlib.pyplot as plt

A = 1
phi1 = 0
phi2 = np.linspace(0, 8 * np.pi, 1000)

y = A * np.exp(1j * phi1) + A * np.exp(1j * phi2)

P = np.abs(y) ** 2.0
plt.close('all')
plt.plot(phi2 / np.pi, P)

L1 = 100e-6
L2 = 1000e-6
n = 1
l = np.linspace(1.4e-6, 1.6e-6, 10000)

f1 = 2 * np.pi / l * L1
f2 = 2 * np.pi / l * L2

y_out = A * np.exp(1j * f1) + A * np.exp(1j * f2)
P_out = np.abs(y_out) ** 2.0

plt.figure()

plt.plot(l/1e-6, P_out)
plt.xlabel('l [mum]')
plt.ylabel('P_out')
c = 3e8
f = c / l
plt.figure()
plt.plot(f/1e12, P_out)
plt.xlabel('f [THz]')
plt.ylabel('P_out')



import numpy as np
import matplotlib.pyplot as plt

n1 = 1.5
D = np.linspace(0.001,0.02,100)
n2 = n1 - D * n1

l = 1.55e-6
a = 4e-6

V = 2 * np.pi * a / l * np.sqrt(n1 ** 2 - n2 ** 2) 

plt.plot(100 * D, V)
plt.xlabel('D [%]')
plt.ylabel('V')

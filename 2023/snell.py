import numpy as np
import matplotlib.pyplot as plt

n1 = 2.0
n2 = 1.0

theta_i = np.linspace(0, np.pi/2, 100)

sin_theta2 = n1 * np.sin(theta_i) / n2
theta2 = np.arcsin( sin_theta2 )

plt.close('all')
plt.plot(theta_i / np.pi * 180, theta2 / np.pi * 180 )
plt.xlabel('theta_i')
plt.ylabel('theta_r') 
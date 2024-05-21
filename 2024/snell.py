import numpy as np
import matplotlib.pyplot as plt

theta_i = np.linspace(0, np.pi/2, 1000)
n2 = 1
n1 = 3
arc_in = n1 * np.sin(theta_i) / n2
theta_2 = np.arcsin( arc_in  ) 
        
plt.close('all')
plt.plot(theta_i, theta_2)
plt.xlabel('theta_i')
plt.ylabel('theta_2')

theta_i_deg = theta_i / np.pi * 180
theta_2_deg = theta_2 / np.pi * 180

plt.plot(theta_i_deg, theta_2_deg)
plt.xlabel('theta_i [Degrees]')
plt.ylabel('theta_2 [Degrees]')

# n2 = 1.5
# n1 = 1
# theta_2 = np.arcsin( n1 * np.sin(theta_i) / n2 ) 
# plt.figure()        
# theta_i_deg = theta_i / np.pi * 180
# theta_2_deg = theta_2 / np.pi * 180

# plt.plot(theta_i_deg, theta_2_deg)
# plt.xlabel('theta_i [Degrees]')
# plt.ylabel('theta_2 [Degrees]')

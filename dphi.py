import numpy as np
import matplotlib.pyplot as plt

def calc_P(dphi):

    E1 = a 
    E2 = a * np.exp(1j * dphi)    
    E = E1 + E2
    return np.abs(E) ** 2
    
l = 1.55e-6
L1 = l
L2 = l + l / 2
a = 1

phi1 = 2 * np.pi / l * L1
phi2 = 2 * np.pi / l * L2
Dphi = phi2 - phi1
Dphi_deg = Dphi / np.pi * 180
print('Phase difference :', Dphi_deg, 'deg')

E1 = a * np.exp(1j * phi1)
E2 = a * np.exp(1j * phi2)

E = E1 + E2
P = np.abs(E) ** 2

Dphi = np.linspace(0, 2*np.pi, 1000)
Ps = np.zeros(Dphi.size)

i = 0
for dphi in Dphi:
    Ps[i] = calc_P(dphi)
    i += 1

plt.close('all')    
plt.plot(Dphi / np.pi * 180, Ps)
plt.xlabel('Dphi [degrees]')
plt.ylabel('P')  
plt.grid()

 
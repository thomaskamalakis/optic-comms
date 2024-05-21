import numpy as np
import matplotlib.pyplot as plt

a_fiber = 0.25
LS = 0.5
l = 20
l_dash = 2
L_exc = 2.5
N = 2 ** np.arange(2, 11)
PS_dBm = -35

Pout_dBm = PS_dBm + a_fiber * l_dash + 2 * LS
Pout = 1e-3 * 10 ** (Pout_dBm/10)

Pin = N * Pout
Pin_dBm = 10 * np.log10( Pin / 1e-3 )
Pin_dBm = Pin_dBm + 2.5

PT_dBm = Pin_dBm + a_fiber * l + 2 * LS

plt.close('all')
plt.figure()
plt.plot(N, PT_dBm, '-o')
plt.xlabel('N')
plt.ylabel('PT [dBm]')
plt.grid()

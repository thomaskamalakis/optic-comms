import numpy as np
import matplotlib.pyplot as plt

def to_dB(x):
    return 10 * np.log10(x)

def to_linear(x):
    return 10 ** (x/10)

class splitter:
    
    def __init__(self, N, 
                       L_additional_dB = 2,
                       L_pol_dB = 0.5,
                       L_uniform_dB = 2):
        self.N = N
        self.L_additional_dB = L_additional_dB
        self.L_pol_dB = L_pol_dB
        self.L_uniform_dB = L_uniform_dB
        
    def calc_loss(self):
        self.L_ideal = 1 / self.N
        self.L_ideal_dB = to_dB(self.L_ideal)
        self.L_dB = self.L_ideal_dB - self.L_additional_dB - self.L_pol_dB - self.L_uniform_dB
        
L1 = 4
L2 = 1
a = 0.2

n = np.arange(1, 8)
N = 2**n
LdB_ideal = np.zeros(N.size)
LdB = np.zeros(N.size)
Ltotal_dB = np.zeros(N.size)
l_splice = 0.4
L_margin = 3

PT = 0
PR = -30
L_tol = PR - PT

for i, Nv in enumerate(N):
    S = splitter(Nv)
    S.calc_loss()
    LdB_ideal[i] = S.L_ideal_dB
    LdB[i] = S.L_dB
    Ltotal_dB[i] = LdB[i] - a * (L1+L2) - 4 * l_splice - L_margin
    
plt.close('all')
plt.figure(1)
plt.plot(N, LdB_ideal, label = 'splitter ideal')
plt.plot(N, LdB, label = 'splitter actual')
plt.plot(N, Ltotal_dB, '-o', label = 'end-to-end')
plt.plot(N, L_tol * np.ones(N.size), '--')
plt.xlabel('N')
plt.ylabel('L_splitter [dB]')
plt.legend()
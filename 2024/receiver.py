import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc, erfinv

def invQ(y):     
    return np.sqrt(2)*erfinv(1-2*y)

def to_dB(x):
    return 10 * np.log10(x)

def to_dBm(x):
    return 10 * np.log10(x/1e-3)

def to_linear(x):
    return 10 ** (x/10)

def to_mW(x):
    return 1e-3 * 10 ** (x / 10)

def Q(x):
    return 0.5 * erfc(x / np.sqrt(2))


qe = 1.60217e-19
kB = 1.380e-23
hP = 6.626e-34
c = 3e8

class receiver:
    
    def __init__(self,
                 l = 1.55e-6,
                 eta = 0.8,
                 Rb = 5e9,
                 RL = 100,
                 FndB = 3,
                 TK = 300,
                 redB = 200):
                 
        self.l = l
        self.eta = eta
        self.Rb = Rb
        self.RL = RL
        self.FndB = FndB
        self.Fn = to_linear(FndB)
        self.TK = TK
        self.f = c / l        
        self.R = eta * qe / (hP * self.f)
        self.Be = self.Rb/2
        self.Pth = 4 * kB * self.Be * self.Fn * TK / self.RL
        self.redB = redB
        self.re = to_linear(redB)
        
    def calc_Pe(self, P1, P0):
        m1 = self.R * P1
        m0 = self.R * P0
        Psh1 = 2 * qe * self.R * P1 * self.Be
        Psh0 = 2 * qe * self.R * P0 * self.Be
        s1 = np.sqrt(self.Pth + Psh1)
        s0 = np.sqrt(self.Pth + Psh0)        
        self.gamma = (m1 - m0) / (s1 + s0)
        self.Pe = Q(self.gamma)
        
    def calc_Pe_Pavg(self, Pavg_dBm):
        self.Pavg_dBm = Pavg_dBm
        self.Pavg = to_mW(Pavg_dBm)
        self.P0 = 2 / (1+self.re) * self.Pavg
        self.P1 = 2 * self.re / (1 + self.re) * self.Pavg
        self.calc_Pe(self.P1, self.P0)
        
    def calc_sens(self, BER):
        g = invQ(BER)
        e = 2 * self.R * (self.re - 1) / (self.re + 1)
        d = 4 * qe * self.R * self.Be * self.re / (1+self.re)
        sth = np.sqrt(self.Pth)
        self.Psens = g ** 2 / e ** 2 * (d + 2 * e / g * sth)
        self.Psens_dBm = to_dBm(self.Psens)
        

Pavg_dBm = np.linspace(-30, -20, 100)
BER = np.zeros( Pavg_dBm.size )
r = receiver()
r.calc_sens(1e-3)
print(r.Psens)
Pavg = r.Psens_dBm
r.calc_Pe_Pavg(Pavg)
print(r.Pe)

# for i, P in enumerate(Pavg_dBm):    
#     r.calc_Pe_Pavg(P)
#     BER[i] = r.Pe

# #plt.close('all')
# plt.semilogy(Pavg_dBm, BER)
# plt.xlabel('Pavg [dBm]')
# plt.ylabel('BER')
# plt.grid()






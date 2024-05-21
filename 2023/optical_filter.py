import numpy as np
import matplotlib.pyplot as plt

def pulse(t, T):
    p = np.zeros(t.size)
    i = np.where( (t > -T/2) & ( t <= T/2) )
    p[i] = 1
    return p
    
Rb = 10e9
T = 1 / Rb
N = 1024
Df_ch = 100e9
t = np.linspace(-10 * T, 10 * T, N)
Dt = t[1] - t[0]
p = pulse(t, T) + pulse(t,T) * np.cos(2 * np.pi * Df_ch * t)

plt.close('all')
plt.plot(t / 1e-12,p)
plt.xlabel('t [ps]')
plt.ylabel('p')

P = np.fft.fftshift( np.fft.fft( np.fft.fftshift(p) ) )
Df = 1 / ( N*Dt )
f = np.arange(-N/2, N/2)*Df
plt.figure()
plt.plot(f/1e9, np.real(P))
plt.xlabel('f [GHz]')
plt.ylabel('P')

B = 5 * Rb
H = np.exp(-f ** 6 / 2 / B**6)

plt.figure()
plt.plot(f/1e9, np.real(P) / np.max(np.real(P) ), label = 'input spectrum')
plt.plot(f/1e9, np.real(H), label = 'transfer function')
plt.legend()

Y = H*P
plt.figure()
plt.plot(f/1e9, np.real(Y) , label = 'output spectrum')
plt.legend()
y = np.fft.fftshift( np.fft.ifft( np.fft.fftshift(Y) ) )
plt.figure()
plt.plot(t/1e-12, np.real(y), label = 'output')
#plt.plot(t/1e-12, np.real(p), label = 'input')
plt.xlim([-2 * T/1e-12, 2 * T/1e-12])
plt.legend()







 

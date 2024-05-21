#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

b2_ps2_Km = 20
b2 = b2_ps2_Km * 1e-27

def gauss(t, t0):
    return np.exp(-t ** 2 / 2 / t0 ** 2)

# create frequency axis
def frequency_axis(t):
    N = t.size
    Dt = t[1] - t[0]
    n = np.arange(-N / 2.0, N / 2.0, 1)
    Df = 1.0 / ( N * Dt)
    return n * Df

# Calculate spectrum of x using FFT
def spectrum(t, x):
    Dt = t[1] - t[0]
    return Dt * np.fft.fftshift(np.fft.fft(np.fft.fftshift(x)))    

def inv_spectrum(f, X):
    Df = f[1] - f[0]
    N = f.size
    return N * Df * np.fft.fftshift(np.fft.ifft(np.fft.fftshift(X)))

def fiber(t, x, b2, L):
    X = spectrum(t, x)
    f = frequency_axis(t)
    Y = X * np.exp(1j * 2 * np.pi ** 2 * f**2 * b2 * L)
    y = inv_spectrum(f, Y)
    return y
    
Rb = 40e9
t0 = 1 / Rb
L1 = 100e3
L2 = 5e3
b2b = -b2 * L1 / L2

t = np.linspace(-20*t0, 20*t0, 4096)
x = gauss(t, t0)

y = fiber(t,x,b2,L1)
z = fiber(t,y,b2b,L2)

plt.close('all')
# plt.plot(f/1e12, np.abs(X), label='initial')
# plt.plot(f/1e12, np.abs(Y), label='final')

# plt.xlabel('frequency [THz]')
# plt.xlim([-5/t0*1e-12, 5/t0*1e-12])
# plt.title('Frequency Domain')
# plt.legend()


plt.figure() 
plt.plot(t / 1e-12, np.abs(y), label = 'fiber-1')
plt.plot(t / 1e-12, np.abs(z), label = 'fiber-2')
plt.plot(t / 1e-12, x, '--', label = 'initial')


plt.xlabel('time [ps]')
plt.xlim([-20*t0/1e-12, 20*t0/1e-12])
plt.title('Time Domain [fiber1-fiber2]')
plt.legend()



y = fiber(t,x,b2b,L2)
z = fiber(t,y,b2,L1)


plt.figure() 
plt.plot(t / 1e-12, np.abs(y), label = 'fiber-2')
plt.plot(t / 1e-12, np.abs(z), label = 'fiber-1')
plt.plot(t / 1e-12, x, '--', label = 'initial')


plt.xlabel('time [ps]')
plt.xlim([-20*t0/1e-12, 20*t0/1e-12])
plt.title('Time Domain [fiber2-fiber1]')
plt.legend()

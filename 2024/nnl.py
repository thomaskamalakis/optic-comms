import numpy as np
import matplotlib.pyplot as plt

def my_box(x, a = 0.0 ):
    return x + a * x ** 2


f0 = 1
T = 10 / f0
N = 1024
A = 4
t = np.linspace(-T/2, T/2, N)
x = A * np.sin(2 * np.pi * f0 * t)

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

y = my_box(x, a=0.1)

f = frequency_axis(t)
X = spectrum(t, x)
Y = spectrum(t, y)

plt.close('all')
plt.figure()
plt.plot(t,x, label='x')
plt.plot(t,y, label='y')

plt.xlabel('t[s]')
plt.ylabel('Signal')
plt.legend()
plt.xlim([0, 2/f0])

plt.figure()
plt.plot(t,np.abs(X), label='X')
plt.plot(t,np.abs(Y), label='Y')

plt.xlabel('f[Hz]')
plt.ylabel('Spectrum')
plt.legend()
plt.xlim([ -3*f0, 3*f0])

A = 10
t = np.linspace(-T/2, T/2, N)
x = A * np.sin(2 * np.pi * f0 * t)
y = my_box(x, a=0.1)
Y2 = spectrum(t, y) 

plt.figure()
plt.plot(t,np.abs(X), label='X')
plt.plot(t,np.abs(Y2), label='Y')

plt.xlabel('f[Hz]')
plt.ylabel('Spectrum')
plt.legend()
plt.xlim([ -3*f0, 3*f0])
 
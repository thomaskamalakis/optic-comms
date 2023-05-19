import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 0.3

def box(x):
    return a*x - b * x ** 2

def linbox(x):
    return a*x

x = np.linspace(0, 1, 100)
y = box(x)
z = linbox(x)

plt.close('all')
plt.figure()
plt.plot(x, y)
plt.plot(x, z)

plt.ylabel('y')
plt.xlabel('x')

t = np.linspace(0, 10, 1000)
f = 1
x1 = 1000*np.cos(2*np.pi*f*t)
plt.figure()
plt.plot(t,x1,label='input')

y1 = box(x1)
plt.plot(t,y1,label='output')
plt.legend()


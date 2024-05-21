import numpy as np
import matplotlib.pyplot as plt

c = 3e8
l0 = 1550e-9
Dl = 100e-9

e = 0.4
Rb = 40e9
B = Rb / e
print('B = ',B/1e9,'GHz')

Df = c / l0 ** 2 * Dl
print('Df = ',Df/1e12,'THz')
N = np.floor( Df / B )
print('Number of channels = ',N)
Rb_tot = N * Rb
print('Total data rate = ', Rb_tot/1e12, 'Tb/s' )









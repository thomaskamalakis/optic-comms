import numpy as np
import matplotlib.pyplot as plt

c = 3e8
l0 = 1550e-9
Dl = 100e-9

l1 = l0 - Dl / 2
l2 = l0 + Dl / 2

f1 = c / l1
f2 = c / l2

Df = f1 - f2
print('Dl=', Dl * 1e9, 'nm', 'Df=', Df / 1e12, 'THz')

Df2 = c / l0 ** 2 * Dl

print('Df  = ', Df/1e12, 'THz')
print('Df2 = ', Df2/1e12, 'THz')

e = np.abs(Df - Df2) / Df
print('Error -> ', e * 100, '%')

coeff = c / l0 ** 2
print('Coeff = ', coeff)
















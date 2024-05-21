#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:25:10 2024

@author: thkam
"""

l0 = 1550e-9
Dl = 100e-9
c = 3e8
es = 0.4

l1 = l0 - Dl/2
l2 = l0 + Dl/2

print('l1 = ',l1/1e-9,'nm')
print('l2 = ',l2/1e-9,'nm')

f1 = c / l1
f2 = c / l2

print('f1 = ',f1/1e12,'THz')
print('f2 = ',f2/1e12,'THz')

Df = c * Dl / (l0**2-Dl**2/4)
Dfb = f1 - f2
print('Df = ',Df/1e12,'THz')
print('Df = ',Dfb/1e12,'THz')

print('l0^2 = ',l0 ** 2)
print('Dl^2 /4 = ',Dl ** 2 / 4)
L = l0 ** 2 / (Dl ** 2/4)
print('L = ', L)

Dfc = c / l0 ** 2 * Dl
print('Dfc = ',Dfc/1e12, 'THz')

Rb = es * Df
print('Rb = ',Rb/1e12, 'Tb/s')

Rb_channel = 40e9

N_ch = Rb / Rb_channel
print('Nch = ',N_ch)







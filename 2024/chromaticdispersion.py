#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

Lmax_Km = 1000

b2_ps2_Km = 20
b2 = b2_ps2_Km * 1e-27

Rb_Gbps = 40
Rb = Rb_Gbps * 1e9

Lmax = Lmax_Km * 1e3

T0 = 1 / Rb
z = np.linspace(0, Lmax)

BF = np.sqrt(1 + (b2 *z / T0 ** 2) ** 2)

plt.close('all')
plt.figure()
plt.plot(z/1e3, BF)
plt.xlabel('z[Km]')
plt.ylabel('BF')





















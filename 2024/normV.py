#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

n1 = 1.5
Dn = np.linspace(0.001, 0.02, 10000)

n2 = n1 - Dn
a = 4e-6
l = 1.55e-6

V = 2 * np.pi * a / l * np.sqrt(n1 ** 2 - n2 ** 2)
x = Dn / n1 * 100

plt.close('all')
plt.plot(x, V)
plt.plot(x, 2.405 * np.ones(n2.size))

plt.grid()
plt.xlabel('Dn [%]')
plt.ylabel('V')


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

b2_ps2_Km = 20
b2 = b2_ps2_Km * 1e-27

Rb_Gbps = np.linspace(2.5, 100, 1000)
Rb = Rb_Gbps * 1e9
T0 = 1/Rb

L = T0 ** 2 / b2
 
plt.close('all')
plt.figure()
plt.semilogy(Rb_Gbps, L/1e3)
plt.xlabel('Rb[Gbps]')
plt.ylabel('L [Km]')





















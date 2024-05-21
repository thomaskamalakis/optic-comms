#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:36:07 2024

@author: thkam
"""

import numpy as np
import matplotlib.pyplot as plt

def to_dB(A):
    return 10 * np.log10(A)

def to_linear(AdB):
    return 10 ** (AdB/10)

adB = 0.2 
l = np.linspace(0, 100, 50)
LdB = -adB * l

plt.close('all')
plt.figure()
plt.plot(l, LdB)
plt.xlabel('Distance [Km]')
plt.ylabel('Loss [dB]')

plt.figure()
plt.plot(l, to_linear(LdB))
plt.xlabel('Distance [Km]')
plt.ylabel('Loss')
plt.grid()



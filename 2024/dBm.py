#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:36:07 2024

@author: thkam
"""

import numpy as np
import matplotlib.pyplot as plt

def to_dBm(P):
    return 10 * np.log10(P / 1e-3)

def to_W(PdBm):
    return 1e-3 * 10 ** (PdBm/10)

P = np.linspace(1e-5, 2e-2, 10000)

plt.close('all')
plt.figure()
plt.semilogx(P/1e-3, to_dBm(P))
plt.xlabel('P [mW]')
plt.ylabel('P [dBm]')
plt.grid()


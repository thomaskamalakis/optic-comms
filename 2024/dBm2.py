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

PRdBm = -1
print('PR [mW] =', to_W(PRdBm) / 1e-3)


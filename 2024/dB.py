#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:36:07 2024

@author: thkam
"""

import numpy as np

def to_dB(A):
    return 10 * np.log10(A)

def to_linear(AdB):
    return 10 ** (AdB/10)

A = 100
print('A = ',A,'--> A[dB] = ', to_dB(A), 'dB')

A = 0.01
print('A = ',A,'--> A[dB] = ', to_dB(A), 'dB')

A = 1
print('A = ',A,'--> A[dB] = ', to_dB(A), 'dB')

AdB = 30
print('A[dB] = ',AdB,'--> A = ', to_linear(AdB))

AdB = -40
print('A[dB] = ',AdB,'--> A = ', to_linear(AdB))



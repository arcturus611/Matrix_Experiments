#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:46:10 2019

@author: arcturus
"""

import numpy as np

def kron_eye(a, b):
    I_1 = np.eye(a)
    I_2 = np.eye(b)
    I_3 = np.kron(I_1, I_2)
    I_4 = np.eye(a*b)
    print('The difference is ', np.sum(I_3 - I_4))
    
    t_3 = np.trace(I_3)
    print('The trace of the Kronecker product is ', t_3)
    t_1 = np.trace(I_1)
    print('The trace of the input to Kronecker product is ', t_1)
    return

if __name__ == '__main__':
    kron_eye(4, 4)
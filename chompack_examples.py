#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:29:12 2019

@author: arcturus
"""
#%%
from cvxopt import spmatrix, amd
import chompack as cp

#%% 
# generate sparse matrix 
I = [0, 1, 3, 1, 5, 2, 6, 3, 4, 5, 4, 5, 6, 5, 6]
J = [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6]
A = spmatrix(1.0, I, J, (7, 7))
symb = cp.symbolic(A, p=amd.order)
print(A)
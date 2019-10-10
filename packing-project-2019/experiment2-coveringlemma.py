#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:14:55 2019
@author: arcturus
"""

#%%
import numpy as np
from numpy import linalg as LA
from scipy.linalg import expm

print_PEp_vs_PEPD_on = 1

#%% generate PSD matrix 
def generate_psd(n):
    scaling_factor = np.random.uniform(1, 100)
    L = np.random.rand(n, n)
    return scaling_factor*L.dot(L.transpose())

#%%
def generate_proj(M, lambda_threshold):
    # INPUT: A psd matrix, and the eigenvalue threshold for "filtering"
    # OUTPUT: A projection matrix formed by thresholding out the large eigenvalues
    (w, v) = LA.eig(M)
    w_mask = w<=lambda_threshold
    w_proj = w_mask.astype(np.int)
    return v.dot(np.diag(w_proj).dot(v.transpose()))

#%%
def test_PEp_vs_PEPD(P, Cp, C, B):
    # We test the following ineq. 
    # Tr(P exp(-Cp)) <= Tr(P exp(-C) P exp(-B))
    LHS = np.trace(P.dot(expm(-Cp)))
    RHS = np.trace(P.dot(expm(-C).dot(P.dot(expm(-B)))))
    result = LHS<=RHS
    if print_PEp_vs_PEPD_on: 
        print("LHS = " + str(LHS))
        print("RHS = " + str(RHS))
        print("result = " + str(result))
    return (LHS<=RHS)

#%% 
if __name__=='__main__':
    num_trials = 1000
    num_rows = 3
    
    for i in range(num_trials):
        C = generate_psd(num_rows)
        B = generate_psd(num_rows)
        Cp = C+B
        
        threshold_scale = np.random.uniform(0.2, 10)
        threshold_lammin = threshold_scale*np.min(LA.eig(C)[0])
        P = generate_proj(C, threshold_lammin)
        
        if test_PEp_vs_PEPD(P, Cp, C, B) is False: 
            print("Case " + str(i) + " FALSE for: Tr(P exp(-Cp)) <= Tr(P exp(-C) P exp(-B))")
            break 
            
        
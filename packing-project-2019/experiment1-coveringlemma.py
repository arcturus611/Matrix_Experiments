#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:48:39 2019
@author: arcturus
"""

import numpy as np
from numpy import linalg as LA
from scipy.linalg import expm 

print_PEp_vs_PEPD_on = 0

#%% generate C
def generate_C(n, m): 
    # INPUT: n = number of matrices (dimension of x), and m = size of each matrix
    # OUTPUT: An n-list of mxm PSD matrices 
    C = []
    smallest_scaling_factor_C = 0.01
    largest_scaling_factor_C = 10
    for i in range(n):
        scale = np.random.uniform(smallest_scaling_factor_C, largest_scaling_factor_C, 1)[0]
        Ci = scale*np.random.rand(m, m)
        C.append(Ci.dot(np.transpose(Ci)))
    min_eigvals = [np.min(LA.eig(C[i])[0]) for i in range(len(C))]
    if (np.min(min_eigvals)<0):
        print("Error: At least one matrix has a negative minimum eigenvalue")
    return C

#%% 
def generate_Cx(C, x):
    rows, cols = np.shape(C[0])
    Cx = np.zeros((rows, rows))
    for i in range(len(C)):
        Cx+= C[i]*x[i]
    return Cx

#%% generate P 
def generate_proj(M, lambda_threshold):
    # INPUT: A psd matrix, and the eigenvalue threshold for "filtering"
    # OUTPUT: A projection matrix formed by thresholding out the large eigenvalues
    (w, v) = LA.eig(M)
    w_mask = w<=lambda_threshold
    w_proj = w_mask.astype(np.int)
    return v.dot(np.diag(w_proj).dot(v.transpose()))

#%% 
def update_x(x, alpha, Delta):
    # FOR NOW: just multiply by 1 + alpha Delta_i for each coordinate, where Delta_i in rand(eps/100, 1/2)
    xp = [x[i]*(1 + alpha*Delta[i]) for i in range(len(x))]
    return xp

#%% 
def generate_x(n):
    return np.random.rand(n)

#%%
def test_PEp_vs_PEPD(P, Cp, C, Cdel):
    # We test the following ineq. 
    # Tr(P exp(-Cp)) <= Tr(P exp(-C) P exp(-delCx))
    LHS = np.trace(P.dot(expm(-Cp)))
    RHS = np.trace(P.dot(expm(-C).dot(P.dot(expm(-Cdel)))))
    result = LHS<=RHS
    if print_PEp_vs_PEPD_on: 
        print("LHS = " + str(LHS))
        print("RHS = " + str(RHS))
        print("result = " + str(result))
    return (LHS<=RHS)

#%% 
def test_PpEp_vs_PEp(Pp, Cp, P): 
    # We test the following inequality (that we already proved an approx version of). 
    # Tr(Pp exp(-Cp)) <= Tr (P exp(-Cp))
    LHS = np.trace(Pp.dot(expm(-Cp)))
    RHS = np.trace(P.dot(expm(-Cp)))
    #print("LHS = " + str(LHS))
    #print("RHS = " + str(RHS))
    #result = LHS<=RHS
    #print("result " + str(result))
    return (LHS<=RHS)

#%%
def test_expx_vs_linapprox(M): 
    # We test the following (matrix) inequality.
    # exp(-M) <=_psd I - M
    LHS = expm(-M)
    RHS = np.identity(np.shape(M)[0]) - 0.5*M
    return np.min(np.linalg.eigvals(RHS - LHS))>=0

#%%
def test_false_statement():
    LHS = 3
    RHS = 5
    return (LHS>=RHS)

#%%
if __name__=='__main__':
    n = 25
    m = 2
    eps = 0.1
    alpha = eps**2
    num_trials = 1000
    
    for i in range(num_trials):
        Delta = np.random.uniform(eps/100, 1/2, n) #line 11 of Alg1 of Mahoney, Rao, Wang, Zhang.
        
        C = generate_C(n, m)
        x = generate_x(n)
        Cx = generate_Cx(C, x)
        
        K = 1.1*np.min(LA.eig(Cx)[0])
        P = generate_proj(Cx, K)
        
        xplus = update_x(x, alpha, Delta)
        Cxplus = generate_Cx(C, xplus)
        Pplus = generate_proj(Cxplus, K)
        
        delCx = generate_Cx(C, alpha*np.multiply(x, Delta))
        
#        if (not test_false_statement()):
#            print("FALSEEEEEEEE")
#            break
        
        if (not test_PEp_vs_PEPD(P, Cxplus, Cx, delCx)):
            print("Case " + str(i) + " FALSE for: Tr(P exp(-Cp)) <= Tr(P exp(-C) P exp(-Cdel))")
            break 

#        if (not test_PpEp_vs_PEp(Pplus, Cxplus, P)):
#            print("Case " + str(i) + " FALSE for: Tr(Pp exp(-Cp)) <= Tr( P exp(-Cp))")
#            break
#        
#        if (not test_expx_vs_linapprox(delCx)): 
#            print("Case " + str(i) + " FALSE for: expm(-M) <= Identity - 0.5*M")
#            break
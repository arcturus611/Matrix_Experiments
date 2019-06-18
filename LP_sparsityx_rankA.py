#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:24:07 2019
This program verifies the following very cool fact.
Given an LP, minimize c^T x subject to Ax = b and x >= 0, 
where rank(A) = r, 
the minimizer x* satisfies nnz(x*) <= r. 
@author: arcturus
"""

#%% 
import numpy as np
import cvxpy as cp

#%% 
def generate_rnd_rnkR_mat(n, d, r):
    U = np.random.rand(n, r)
    V = np.random.rand(d, r)
    S = np.diag(np.random.rand(r))
    return U.dot(S.dot(V.transpose()))

#%% 
if __name__ == '__main__':
    n = 20
    d = 15
    r = 18
    eps = 0.01
    
    # By *first* generating a feasible x and THEN 
    # creating b = Ax, we ensure that our constraint set is 
    # feasible. 
    x_feas = np.random.rand(d)
    A = generate_rnd_rnkR_mat(n, d, r)
    b = A.dot(x_feas)
    c = np.random.rand(d)
    
    x = cp.Variable(d)
    constraints= [A@x == b]
    constraints+= [x>= 0]
    
    prob = cp.Problem(cp.Minimize(c.T@x), constraints)
    prob.solve()
    print("The optimal value is ", prob.value)
    print("The optimizer is ", x.value)
    print("The number of non-zero entries in the optimizer is ", np.sum(x.value>eps))
    print("The rank of the constraint matrix is ", r)
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:40:18 2019

@author: arcturus
"""
#%% The conjecture was, ||ABA||_op <= ||A^2 B||_op. Conjecture disproved. 
# Next conjecture, ||ABAt||_op <= ||At A B||_op, B not necessarily symmetric. Conjecture disproved (MANY RANDOM TRIALS NEEDED, saved to "operatornorm_conj1.txt')
# Next conjecture, ||ABAt||_op <= ||At A B||_op, B symmetric. True so far... 
# Next conjecture, ||ABA||_op <= ||A^2 B||_op when A and B are symmetric. True for 1 million random cases. 

import numpy as np

def main():
    n = 6
    A = np.random.rand(n, n)
#    A = (A + A.transpose())*0.5
    B = np.random.rand(n, n)
    B = (B + B.transpose())*0.5
    ABAt = A.dot(B.dot(A.transpose()))
    ABAt_op = np.linalg.norm(ABAt, 2) #largest singular value
    AtAB = (A.transpose()).dot(A.dot(B))
    AtAB_op = np.linalg.norm(AtAB, 2)
    
    #print("The operator norm of ABA is ",ABA_op)
    #print("The operator norm of A2B is ",A2B_op)

    return A, B, ABAt_op, AtAB_op

#%% 
if __name__ == '__main__':
    #%% 
    [A, B, ABAt_op, AtAB_op] = main()
    count = 0
    while((ABAt_op<=AtAB_op) and (count < 100000)):
        [A, B, ABAt_op, AtAB_op] = main()   
        count = count + 1
    if (ABAt_op > AtAB_op): 
        print("Conjecture disproved")
        with open("operatornorm_conj2.txt", "a") as f:
                f.write('Conjecture: opnorm(ABAt) <= opnorm(AtAB) when B symmetric: disproved by example.\n\n')
                f.write('A: \n')
                np.savetxt(f, A, delimiter = ",")
                f.write('\n\n B: \n')
                np.savetxt(f, B, delimiter = ",")
            
            
           
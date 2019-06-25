#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:35:21 2019

@author: arcturus
"""

import numpy as np

def main():
    A = np.random.rand(4, 7)
    M = np.random.rand(4, 4)
    M = (M + np.transpose(M))*0.5
    AtMA = np.transpose(A).dot(M.dot(A))
    print("The operator norm of AtMA is: ", np.linalg.norm(AtMA, 2))
    print("The operator norm of M is: ", np.linalg.norm(M, 2))
    print("The product of the three operator norms is: ", np.linalg.norm(M, 2)*((np.linalg.norm(A))**2))

if __name__ =='__main__':
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:18:39 2019

@author: arcturus
"""

import matplotlib.pyplot as plt
import numpy as np

if __name__=='__main__':
    y = np.array([2.000064, 2.000448, 2.001118, 2.001957, 2.010314, 2.024801, 2.044183, 2.057085, 2.067488, 2.093981, 2.123097, 2.154399, 2.187543, 2.222256, 2.258317, 2.295544, 2.333789, 2.372927, 2.453481, 2.536550, 2.621644, 2.708400, 2.796537, 3.021591, 3.251640, 3.721503, 4.199712, 5.171210, 6.157233])
    x = np.array([0.32, 0.33, 0.34, 0.35, 0.40, 0.45, 0.50, 0.5286, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.75, 2.00, 2.50, 3.00, 4.00, 5.00])
    t1 = 2
    y1 = 3.251640
    t2 = 1.68567
    y2 = 2.96370
    t = np.linspace(t2, t1, 50)
    y_lin2 = (y1*(t - t2) - y2*(t - t1))/(t1-t2)#y = (y1*(x-x2) - y2(x-x1))/(x1-x2)
#    y_lin2s = 0.9201960000000007*t + 1.4112480000000005
    omega1 = 2.32
    y_lin3 = 1 + (t/2)*omega1 #good until 2.32
#    y_lin4 = 1.43 + 0.91021*t
#    start_idx = np.where(x==1.75)[0][0]
#    end_idx = np.where(x==2)[0][0]
    plt.plot(t, y_lin2, 'r-', label='($\omega(t_1)$*(t - $t_2$) - $\omega(t_2)$*(t - $t_1$))/($t_1 - t_2$)')
    plt.plot(t, y_lin3, 'k-', label='1+$\omega(1)$*t/2')#, t, y_lin4, 'bo')
    plt.xlabel('$t (= 2/a)$, where $a = \log_n m$')
    plt.ylabel('$y = \omega(t)$')
    plt.title('Upper bound check on $\omega$ over $a \in [1, \omega(1)/2]$')
    plt.legend(loc = 'lower right')
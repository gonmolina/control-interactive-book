#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:27:30 2020

@author: jpp
"""
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,12,200)
wn=1
xi=[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0]

fig, ax = plt.subplots(figsize=(8, 5))
#line, = ax.plot(t, s, lw=3)

for i in range(11):
    G=ctrl.tf(wn**2,[1,2*xi[i]*wn,wn**2])
    t,y=ctrl.step_response(G,T=t)
    plt.plot(t,y)
    indice=np.where(t>=3)
    plt.text(3,y[(indice[0][0])], r'$\xi$ = %s'%xi[i])

plt.grid()
plt.xlabel(r'$\omega_n$ t')
plt.ylabel('y(t)')
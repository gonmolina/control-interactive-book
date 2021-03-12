#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:14:47 2020

@author: jpp
"""
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

G=ctrl.tf(1,[1,0])
ctrl.pzmap(G)
plt.figure()
ctrl.bode(G,dB=True)

#%%

G=ctrl.tf(1,[1,0,0])
ctrl.pzmap(G)
plt.figure()
ctrl.bode(G,dB=True)

#%%
G=ctrl.tf(1,[1,1])
ctrl.pzmap(G)
plt.figure()
ctrl.bode(G,dB=True)

#%%
xi=[0.9,0.7,0.5,0.3,0.1,0.01]
wn=1
G=ctrl.tf(wn**2,[1,2*xi[2]*wn,wn**2])
ctrl.pzmap(G)
plt.figure()
for i in range(np.size(xi)):
    G=ctrl.tf(wn**2,[1,2*xi[i]*wn,wn**2])
    ctrl.bode(G,dB=True)

#%%
G=ctrl.tf([1,0],1)
ctrl.pzmap(G)
plt.figure()
ctrl.bode(G,dB=True)

#%%

G=ctrl.tf([1,0,0],1)
ctrl.pzmap(G)
plt.figure()
ctrl.bode(G,dB=True)

#%%
G=ctrl.tf([1,1],1)
ctrl.pzmap(G)
plt.figure()
ctrl.bode(G,dB=True)

#%%
xi=[0.9,0.7,0.5,0.3,0.1,0.01]
wn=1
plt.figure()
for i in range(np.size(xi)):
    G=ctrl.tf([1,2*xi[i]*wn,wn**2],wn**2)
    ctrl.bode(G,dB=True)

#%%
G=ctrl.tf([1,-1],1)
ctrl.pzmap(G)
plt.figure()
ctrl.bode(G,dB=True)

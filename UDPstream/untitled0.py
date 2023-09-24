# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:10:57 2020

@author: choms
"""

import numpy as np

#arr = np.array([0,1, 2, 3, 4, 5, 6, 7,8,9])
#
#print(np.sum(arr[0:5]))
#print(np.sum(arr[5:10]))

s = (2000,50)


z=np.ones(s)
print(z)
print(z.shape)

y=z.shape[0]
x=z.shape[1]
dv=100
yr=y/dv

frq=[]
for i in range(int(yr)):
    frq.append(np.sum(z[i*dv+0:i*dv+dv,:],axis=0))
    
sptg=np.array(frq).astype('float')
print(sptg.shape)
print(sptg[0,:])
print(sptg[:,0])
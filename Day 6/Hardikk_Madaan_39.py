# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:49:44 2018

@author: Hardikk Madaan
"""

import numpy as np
x= np.random.randint(5,15,40)
counts= np.bincount(x)
print (np.argmax(counts))

(values,counts) = np.unique(x,return_counts=True)
ind=np.argmax(counts)
print (values[ind]) 
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:34:23 2018

@author: Hardikk Madaan
"""

import numpy as np
import matplotlib.pyplot as plot
incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes)

plot.hist(incomes,50)
plot.show()
np.mean(incomes)
np.median(incomes)

incomes = np.append(incomes , [1000000])

np.mean(incomes)
np.median(incomes)
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:42:59 2018

@author: Hardikk Madaan
"""

import numpy as np
incomes = np.random.normal (150, 20, 1000)

import matplotlib.pyplot as plot

plot.hist(incomes,100)
plot.show()
np.std(incomes)
np.var(incomes)
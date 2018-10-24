# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:45:33 2018

@author: Hardikk Madaan
"""

import pandas as pd
ship =pd.read_csv("training_titanic.csv")
ship['Child'] = 0

ship['Child'][ship['Age'] < 18 ] = 1

ship['Survived'][ship['Child']==1].value_counts(normalize=True)
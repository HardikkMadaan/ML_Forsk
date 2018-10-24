# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:48:41 2018

@author: Hardikk Madaan
"""


import pandas as pd
df = pd.read_csv("Loan.csv")
features = df.iloc[:,[0,1,2,3,4,5,6,7,9,10,11,12]].values
labels = df.iloc[:,8].values
features = pd.get_dummies(features,columns='Property_Area')







# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:55:05 2018

@author: Hardikk Madaan
"""

import pandas as pd
df = pd.read_csv("Bahubali2_vs_Dangal.csv")
features  = df.iloc[:,0:1].values
labelsb = df.iloc[:,1].values
labelsd = df.iloc[:,2].values

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labelsb)
bahub10 =  regressor.predict(10)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labelsd)
dangal =  regressor.predict(10)
if dangal > bahub10:
    print ("Dangal had more earnings")
else:
    print ("Bahubali had more earnings")
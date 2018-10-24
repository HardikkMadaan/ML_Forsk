# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 07:24:36 2018

@author: Hardikk Madaan
"""

import pandas as pd
import numpy as np
df = pd.read_csv("stats_females.csv")
features = df.iloc[:,1:].values
labels = df.iloc[:,0].values

from sklearn.cross_validation import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)

pred = regressor.predict(features_test)        


import statsmodels.formula.api as sm
features = np.append(arr = np.ones((214,1)).astype(int), values = features , axis =1)
features_opt = features[:,[0,1,2]]
regressor_OLS = sm.OLS(endog = labels,exog = features_opt).fit()
regressor_OLS.summary()                     


features_opt = features[:,[1,2]]
regressor_OLS = sm.OLS(endog = labels,exog = features_opt).fit()
regressor_OLS.summary()                     
print ("Yes,both predictors are significant to predict a student's height")
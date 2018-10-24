# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:46:10 2018

@author: Hardikk Madaan
"""

import pandas as pd
import numpy as np
dataset = pd.read_csv("iq_size.csv")
features  = dataset.iloc[:,1:].values
labels = dataset.iloc[:,0].values

from sklearn.cross_validation import train_test_split
features_train , features_test,labels_train,labes_test = train_test_split(features,labels,test_size = 0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)


x = np.array([90,70,150]).reshape(1,-1)
print (regressor.predict(x))

import statsmodels.formula.api as sm
features = np.append(arr = np.ones((38,1)).astype(int), values = features , axis =1)
features_opt = features[:,[0,1,2,3]]
regressor_OLS = sm.OLS(endog = labels,exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[0,1,2]]
regressor_OLS = sm.OLS(endog = labels,exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[1,2]]
regressor_OLS = sm.OLS(endog = labels,exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[1]]
regressor_OLS = sm.OLS(endog = labels,exog = features_opt).fit()
regressor_OLS.summary()

print ("Brain is the most udeful in predicting PIQ")

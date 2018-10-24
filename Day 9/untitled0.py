# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 17:27:56 2018

@author: Hardikk Madaan
"""

import pandas as pd
import numpy as np
dataset=pd.read_csv("Salary_Classification.csv")
features = dataset.iloc[:,:-1].values
labels= dataset.iloc[:,-1].values
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,0]  =labelencoder.fit_transform(features[:,0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

#AVOIDING THE DUMMY VARIABLE TRAP
features = features[:,1:]
from sklearn.cross_validation import train_test_split
features_train , features_test,labels_train,labes_test = train_test_split(features,labels,test_size = 0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)

pred = regressor.predict(features_test)
                             
x= np.array([0,0,1150,3,4]).reshape(1,-1)
print (regressor.predict(x))

score1= regressor.score(features_train,labels_train)
score2 = regressor.score(features_test,labes_test)

import statsmodels.formula.api as sm
'''now we will check for the features which are most important and play a 
major role in prediction
'''
features = np.append(arr = np.ones((30,1)).astype(int), values = features , axis =1)
features_opt = features[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = labels,exog = features_opt).fit()
regressor_OLS.summary()
'''
now one by one we will remove the features with the Pvalue more than 5%
data with pValues less than 5% will be kept
'''
features_opt = features[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = labels,exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[0,1,3,5]]
regressor_OLS = sm.OLS(endog = labels,exog = features_opt).fit()
regressor_OLS.summary()



features_opt = features[:,[0,3,5]]
regressor_OLS = sm.OLS(endog = labels,exog = features_opt).fit()
regressor_OLS.summary()




features_opt = features[:,[0,5]]
regressor_OLS = sm.OLS(endog = labels,exog = features_opt).fit()
regressor_OLS.summary()




'''
THE ABOVE ACTIVITY THAT WE DID WAS TO FIND OUT THE MOST IMPORTANT FEATURE
THE ACTIVITY IS KNOWN AS DIMENSION REDUCTION IN MACHINE LEARNING
'''
print (regressor.coef_)
'''
USING THE ABOVE FUNCTION
WE SEE THE WEIGHT AND THUS GET TO KNOW ABOUT THE MOST IMPROTANT FEATURE.JUST ANOTHER ALTERNATIVE TO FINDING PVALUES AND ALL
'''












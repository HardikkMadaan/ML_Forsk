# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:29:05 2018

@author: Hardikk Madaan
"""

'''Machine learning is of two types
1) supervised having both features and labels
a)regression
-- linear
-- multiple
-- polynomial
b)classification
-- logistic regression
-- 
2)unsupervised having only features
'''

#LEARNING PLOYNOMIAL REGRESSION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

dataset = pd.read_csv("Position_Salaries.csv")
features = dataset.iloc[:,1:2].values
labels = dataset.iloc[:,2].values

#TRYING OUT IT WITH LINEAR REGRESSION
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features,labels)


print (lin_reg.predict(6.5))


#VISUALISING LINEAR REGRESSION
plot.scatter(features,labels,color='red')
plot.plot(features,lin_reg.predict(features),color='blue')
plot.show()

#FITTING POLYNOMIAL REGRESSION INTO DATASET
from sklearn.preprocessing import PolynomialFeatures
poln_object = PolynomialFeatures(degree = 4)
features_poly = poln_object.fit_transform(features)

lin_reg2  =LinearRegression()
lin_reg2.fit(features_poly,labels)

print(lin_reg2.predict(poln_object.fit_transform(6.5)))

#   VISUALISING POLYNOMIAL REGRESSION CURVE
plot.scatter(features,labels,color='red')
plot.plot(features,lin_reg2.predict(features_poly),color='blue')
plot.show()


#VISUALISING  THE RESULTS OF POLYNOMIAL REGRESSION IN HIGGHER RESOLUTION
features_grid = np.arange(min(features),max(features),0.1)
features_grid = features_grid.reshape((-1,1))
plot.scatter(features,labels,color='red')
plot.plot(features_grid,lin_reg2.predict(poln_object.fit_transform(features_grid)),color='blue')
plot.show()






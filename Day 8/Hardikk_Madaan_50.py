# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:40:20 2018

@author: Hardikk Madaan
"""

import pandas as pd
df = pd.read_csv("Foodtruck.csv")
features = df.iloc[:,0:1].values
labels  =df.iloc[:,1].values
from sklearn.cross_validation import train_test_split
features_train,features_test,labels_train,labels_test= train_test_split(features,labels,test_size=0.2,random_state=0)


import numpy as np
import matplotlib.pyplot as plot
from sklearn.linear_model import LinearRegression
regressor  = LinearRegression()
regressor.fit(features_train,labels_train)
regressor.predict(3.073)
labels_pred = regressor.predict(features_test)
score = regressor.score(features_test,labels_test)
score2 = regressor.score(features_train,labels_train)

plot.scatter(features_train,labels_train , color='red')
plot.plot(features_train,regressor.predict(features_train),color='blue')
plot.title('Population vs Income  (Training Set)')
plot.xlabel('Population')
plot.ylabel('Income')
plot.show()

plot.scatter(features_test,labels_test , color='red')
plot.plot(features_train,regressor.predict(features_train),color='blue')
plot.title('Population vs Income (Test Set)')
plot.xlabel('Population')
plot.ylabel('Income')
plot.show()
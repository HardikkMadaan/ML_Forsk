# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:40:45 2018

@author: Hardikk Madaan
"""

import pandas as pd
dataset=pd.read_csv("Cricket_Salary_Data.csv")
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)
#Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
festures_test = sc.transform(features_test)

#BEST FIT LINE
'''
TO FIND A LINE PASSING THROUGH THE DATASET HAVING THE VALUE D1(SQ) + D2(DQ)...
MINIMUM
D1 IS THE DISTANCE FROM POINT ONE TO THE LINE
AND SQ IS SQUARE OF THE VALUE
'''

import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
dataset= pd.read_csv("Income_Data.csv")
features  = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values

#SPLITTING THE DATASET
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

#FITTING LINEAR REGRESSION TO THE TRAINING DATA
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)
regressor.predict(6.5)
regressor.predict(12)

#PREDICTING THE TEST SET RESULTS
labels_pred = regressor.predict(features_test)

#VISUALISING THE TRAINING DATA SET
plot.scatter(features_train,labels_train , color='red')
plot.plot(features_train,regressor.predict(features_train),color='blue')
plot.title('Income vs Experience (Training Set)')
plot.xlabel('ML-Experience')
plot.ylabel('Income')
plot.show()

plot.scatter(features_test,labels_test , color='red')
plot.plot(features_train,regressor.predict(features_train),color='blue')
plot.title('Income vs Experience (Test Set)')
plot.xlabel('ML-Experience')
plot.ylabel('Income')
plot.show()

#model Score
score = regressor.score(features_test,labels_test)
score2 = regressor.score(features_train,labels_train)




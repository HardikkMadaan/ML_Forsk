# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:07:33 2018

@author: Hardikk Madaan
"""

'''
INDEPENDNT VARIABLES ARE CALLED FEATURES
DEPENDENT VARIABLES ARE CALLED LABELS

WE MUST HAVE LABELED DATA SET FOR PREDICTION
THE DATA SET HAVING BOTH FEATURES AND LABELS THEN THAT CASE IS CALLED SUPERSVIED
MACHINE LEARNING

DATA SET HAVING ONLY FEATURES/INDEPENDENT VARIABLES AND NO LABELS , IT IS 
KNOWN AS UNSUPERVISED MACHINE LEARNING
'''
'''
THE ENTIRE DATA WILL BE DIVIED IN TWO PARTS
1 ) TRAINING CONSISTING OF FEATURES AND LABELS
2 ) TEST CONSISTING OF FEATURES AND LABELS
FIRST WE TRAIN USING TRAINING DATA
THEN WE CHECK USING TEST GIVING ONLY FEATURES THEN WE CHECK THE PREDICITON USING
LABELS OF TEST DATA
'''
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

#IMPORTING THE DATASET
dataset = pd.read_csv("Data.csv")
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,3].values
'''SPLITTING THE DATA IN TRAINING AND TESTING AND FURTHER IN FEATURES AND 
LABELS FOR EACH USING SCIKIT LEARN LIBRARY
'''
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)


#cricket task

dataset  =pd.read_csv("Cricket_Salary_Data.csv")
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values
#Taking care of missing data using Imputer
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer = imputer.fit(features[:,1:2])
features[:,1:2]=imputer.transform(features[:,1:2])

'''
CONVERYING CATEGORICAL DATA TO NUMERICAL FORM IS NKWON AS LABEL ENCODING'''
#ENCODING CATEGORICAL DATA(TEXTUAL DATA) EACH TEXT IS ASIGNED A UNIQUE NUMBER
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features [:,0]= labelencoder.fit_transform(features[:,0])


'''
LABEL ENCODING :GENERATES AN ORDER .SO WHERE WE DATA IS NOT IN ORDER AND CAN BE
ANYTHING, THERE WE USE ONEHOT ENCODING .
FOR EXAMPLE DAYS OF A WEEK. THEY DONT NEED TO BE IN ANY ORDER SO WE USE. ONE HOT
ENCODING AND FOR EXAMPLE EDUCATIONAL QULAIFICATION , THERE WE USE LABEL ENCODING


PANDAS DOES ONEHOT ENCODING DIRECTLY 
AND 
SCIKIT LEARN WE FIRST USE LABELENCODING AND THEN USE ONEHOTENCODINNG
'''
#oneHot encoding
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[0])
features = onehotencoder.fit_transform(features).toarray()

#Encoding the dependent variable
labels = labelencoder.fit_transform(labels)

#SPLITTING DATA SET INTO TRAINING AND TEST DATA
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)











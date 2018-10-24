# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:24:44 2018

@author: Hardikk Madaan
"""

import pandas as pd
df = pd.read_csv("Loan.csv")
features = df.iloc[:,[0,1,2,3,4,5,6,7,9,10,11,12]].values
labels = df.iloc[:,8].values


from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features [:,1]= labelencoder.fit_transform(features[:,1])
features [:,2]= labelencoder.fit_transform(features[:,2])
features [:,3]= labelencoder.fit_transform(features[:,3])
features [:,4]= labelencoder.fit_transform(features[:,4])
features [:,5]= labelencoder.fit_transform(features[:,5])
features [:,11]= labelencoder.fit_transform(features[:,11])
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[0])
features[:,11] = onehotencoder.fit_transform(features[:,11])
labels = labelencoder.fit_transform(labels)


from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)


# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 19:01:11 2018

@author: Hardikk Madaan
"""

import pandas as pd
Dataset = pd.read_csv("Cars.csv")
features = Dataset.iloc[:,1:].values
labels = Dataset.iloc[:,0].values
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.5,random_state=0)
df = pd.DataFrame(features)
df.to_csv("features.csv",index=False)
df = pd.DataFrame(labels)
df.to_csv("labels.csv",index=False)
df = pd.DataFrame(features_test)
df.to_csv("features_test.csv",index=False)
df = pd.DataFrame(features_train)
df.to_csv("features_train.csv",index=False)
df = pd.DataFrame(labels_test)
df.to_csv("labels_test.csv",index=False)
df = pd.DataFrame(labels_train)
df.to_csv("labels_train.csv",index=False)
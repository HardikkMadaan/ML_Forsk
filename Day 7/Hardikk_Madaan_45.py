# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 19:34:14 2018

@author: Hardikk Madaan
"""

import pandas as pd
Dataset= pd.read_csv("Automobile.csv")
print (Dataset.dtypes)
Columns = Dataset.select_dtypes(include=['object'])

Dataset = Dataset.fillna(Dataset.mean())

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
Dataset['body_style']= labelencoder.fit_transform(Dataset['body_style'])


Dataset['drive_wheels']= labelencoder.fit_transform(Dataset['drive_wheels'])
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder()
Dataset['drive_wheels'] = onehotencoder.fit_transform(Dataset['drive_wheels'])


from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder()
Dataset['body_style'] = onehotencoder.fit_transform(Dataset['body_style'])
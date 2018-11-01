# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:58:06 2018

@author: Hardikk Madaan
"""

#LEARNING LOSITICS REGRESSION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("Social_Network_Ads.csv")
features = dataset.iloc[:,[2,3]].values
labels = dataset.iloc[:,4].values

#SPLITTING
from sklearn.cross_validation import train_test_split
features_train, features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.25,random_state=0)



#FEATURE SCALING
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

#FITTING LOGISTIC REGRESSION INTO TRAINING SET
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train,labels_train)


#PREDICTING THE RESULTS
labels_pred = classifier.predict(features_test)


#MAKING THE CONFUSION MATRIX
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)


#VISUALISING TRAINING DATA SET
from matplotlib.colors import ListedColormap
features_set,labels_set = features_train,labels_train
features1,features2 = np.meshgrid(np.arange(start = features_set[:,0].min()-1,stop = features_set[:,0].max()+1,step = 0.01),
 np.arange(start = features_set[:,1].min()-1,stop =features_set[:,1].max() + 1,step   = 0.01))
plt.contourf(features1,features2,classifier.predict(np.array([features1.ravel(),features2.ravel()]).T).reshape(features1.shape),
  alpha  = 0.75,cmap=ListedColormap(('red','green')))                                                            
plt.xlim(features1.min(),features1.max())
plt.ylim(features2.min(),features2.max())
for i,j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set ==j,0],features_set[labels_set ==j,1],
                c = ListedColormap(('red','green'))(i),label=j)
plt.title('Logistic Regression (Training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()


#VISUALISING TEST DATA SET
from matplotlib.colors import ListedColormap
features_set,labels_set = features_test,labels_test
features1,features2 = np.meshgrid(np.arange(start = features_set[:,0].min()-1,stop = features_set[:,0].max()+1,step = 0.01),
 np.arange(start = features_set[:,1].min()-1,stop =features_set[:,1].max() + 1,step   = 0.01))
plt.contourf(features1,features2,classifier.predict(np.array([features1.ravel(),features2.ravel()]).T).reshape(features1.shape),
  alpha  = 0.75,cmap=ListedColormap(('red','green')))                                                            
plt.xlim(features1.min(),features1.max())
plt.ylim(features2.min(),features2.max())
for i,j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set ==j,0],features_set[labels_set ==j,1],
                c = ListedColormap(('red','green'))(i),label=j)
plt.title('Logistic Regression (Training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()




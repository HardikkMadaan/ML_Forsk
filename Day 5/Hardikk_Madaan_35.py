# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:20:22 2018

@author: Hardikk Madaan
"""

import pandas as pd
ship = pd.read_csv("training_titanic.csv")

'''How many people in the given training set survived the disaster with
 the Titanic and how many of them died? '''
ship['Survived'].value_counts() 

'''Calculate and print the survival rates as
 proportions (percentage) by setting the normalize argument to True.'''
ship['Survived'].value_counts(normalize=True) 

'''Repeat the same calculations but on subsets of survivals based on Sex:'''

'''Males that survived vs males that passed away'''
ship['Survived'][ship['Sex'] == 'male'].value_counts()

'''Females that survived vs Females that passed away'''
ship['Survived'][ship['Sex'] == 'female'].value_counts()

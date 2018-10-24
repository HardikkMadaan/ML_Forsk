# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:43:49 2018

@author: Hardikk Madaan
"""

import pandas as pd
df = pd.read_csv("Automobile.csv")

df['price'] = df['price'].fillna(df['price'].mean())
import numpy as nd
price = nd.array(df['price'])
nd.min(price)
nd.max(price)
nd.average(price)
nd.std(price)
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 19:41:51 2018

@author: Hardikk Madaan
"""
import re
N = input("Enter a number")
if re.match(r'[\+\.-]?[0-9]*\.[0-9]+',N):
    print ("True")
else:
    print ("False")
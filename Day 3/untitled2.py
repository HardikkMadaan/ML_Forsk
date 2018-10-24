# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:15:01 2018

@author: Hardikk Madaan
"""

import re
T= input()

while T!=0:

    N = input()
    if re.match(r'[\+\.-]?[0-9]*\.[0-9]+',N):
        print ("True")
    else:
        print ("False")
    
T=T-1

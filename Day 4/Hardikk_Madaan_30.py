# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:20:32 2018

@author: Hardikk Madaan
"""

url= "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
import requests
page = requests.get(url).text
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)

right_table=soup.find('table',class_='table')

A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_table.findAll("tr"):
    
    cells = row.findAll('td')
    if len(cells)==5:
        A.append(cells[0].find(text=True))
        B.append(cells[1].text.strip())
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))

import pandas as pd
dq=pd.DataFrame(A[1:],columns=["Pos."])
dq["Team"]=B[1:]
dq["Matches"]=C[1:]
dq["Points"]=D[1:]
dq["Rating"]=E[1:]

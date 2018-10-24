# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 18:42:10 2018

@author: Hardikk Madaan
"""
url= "https://wordpandit.com/29-states-capitals/"
import requests
page = requests.get(url).text
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)

right_table=soup.find('table',class_='alignleft')

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll("tr"):
    
    cells = row.findAll('td')
    
    A.append(cells[0].find(text=True))
    B.append(cells[1].find(text=True))
    C.append(cells[2].find(text=True))
    D.append(cells[3].find(text=True))
    E.append(cells[4].find(text=True))
    F.append(cells[5].find(text=True))
    
import pandas as pd
df=pd.DataFrame(A[1:],columns=["S.no."])
df["States"]=B[1:]
df["Capital"]=C[1:]
df["Chief Minister"]=D[1:]
df["Political Party"]=E[1:]
df["Governer"]=F[1:]
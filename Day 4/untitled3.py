# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:29:08 2018

@author: Hardikk Madaan
"""

url ="https://en.wikipedia.org/wiki/List_of_Asian_countries_by_GDP"
import requests
page = requests.get(url).text
from bs4 import BeautifulSoup
soup= BeautifulSoup(page)
table =soup.find('table',{'class':"wikitable sortable"})
links=table.findAll('a')
Countries =[]
for item in links:
    Countries.append(item.get('title'))


A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in table.findAll("tr"):
    
    cells = row.findAll('td',{'style':"text-align:left;"})
    if len(cells)==5:
        A.append(cells[0].find(text=True))
        B.append(cells[1].text.strip())
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
    
import pandas as pd
df=pd.DataFrame()
df['Countries']=Countries
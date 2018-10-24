# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:54:36 2018

@author: Hardikk Madaan
"""

#REST API URL
url = "http://api.openweathermap.org/data/2.5/weather"
url+="?q=Jaipur&APPID=c94d173aa0dfc8df5557952abe5b14a3"


#USING URLIB2 LIBRARY
import requests
resp = requests.get(url)  # GET request to REST API
print (resp.text)         # prints the server Response

"""
Python 3 users cannot use urllib2
# Using urllib2 library
import urllib2

resp = urllib2.urlopen(url)   # GET request to REST API

print resp.read()   # prints the server Response
"""
import requests
data = {
        "Name":"Pankaj Kumar",
        "Age":"18",
        "College":"Manipal",
        "Phone_Number":"+91-9927385960",
        "Branch":"CSE"
        }
        
data = {
        "Phone_Number":"9414291932",
        "Name":"James Bond", 
        "College_Name":"Haward",
        "Branch":"CSE"
        }
        
send_url = "http://13.127.155.43/api_v0.1/sending"
send_req = requests.post(send_url, json=data)
print (send_req.text)

receive_url = "http://13.127.155.43/api_v0.1/receiving?Phone_Number=9414291932"
receive_req = requests.get(receive_url)
print (receive_req.text)

#version 2

import urllib2
import json

send_url = "http://13.127.155.43/api_v0.1/sending"
data = {
        "Phone_Number" : "9887765324",
        "Name" : "James Bond",
        "College_Name" : "Harward",
        "Branch" : "CSE"
        }
data = json.dumps(data)
header = {"Content-Type" : "application/json"}
request = urllib2.Request(send_url,data,headers=header)
send_response = urllib2.urlopen(request)
print (send_response.read())





























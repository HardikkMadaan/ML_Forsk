# -*- coding: utf-8 -*- 
"""
Created on Wed Sep 26 17:16:52 2018

@author: Hardikk Madaan
"""

dict1 = {'fname':'John', \
         'lname':'Miller', \
         'profession':'plumber', \
         'age':'32'}

dict1['age']

dict1['fname']= 'James'

dict1.items()  #list of all the items in the dictionary in the form of tuples
dict1.keys()   #list of keys in the form of tuples
dict1.values()

for key in dict1.keys():
    print (key)

for items in dict1.values():
    print (items)
                    
for k,v in dict1.items():
    print (v,k)


words = ['one','two','one','two','three','four','one']
words.count('two')

freq = dict()
for word in words:
    if word in freq:
        freq[word]= freq[word] + 1
    else:
        freq[word]=1

college= "Manipal Jaipur"
letter = dict()
for lett in college:
    if lett in letter:
        letter[lett] = letter[lett] + 1
    else:
        letter[lett] = 1

"""
In regular expression 
\d will search for all digits
\D will search for everything other than digit
[^abc] will search for everything other than abc
^abc will search for abc in a string starting with abc
abc$ will search for abc in a string ending abc
\w alpha numberic
\W anti alpha numeric
\s spaces
\S anti spaces
(abc\def) either abc of def
[abc] a or b or c
[a-c]+\.{4}[d-f]+                        + means a or b or c one should be there atleast once
                                         and then four dots and then d or e or f should be 
                                         there at least once
[a-c]*\.{4}[d-f]+                       Here the minimum occurence of a or b or c can be zero
?                                       means occurence can be zero or one

^[a-z0-9_-]{3,16}$       given in brackets are the characters allowed._ and - are
                        also allowed and length should be minimum 3 and max 16
                        and ^ says start and $ says ends

^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,8})$          This expression will help in 
                                                      searching for email address.
                                                      
* zero or more occurence
+  one or more occuuerence
? zero or one occurence
"""
# use import re to import regular expression library
# re means regular expression
#Match   search where it is in the begining
#search   search anywhere first occurence only
#find all return all the matching entries
'''
result = re.findall(r'\d{2}-\d{2}-\d{2}',Here we enter the data)
'''
l1=['+91-9910710891',\
    '999999-9999',\
    '99999x99999']
    
import re
for val in l1:
    if re.match(r'\+[0-9]{2}-[8-9]{1}[0-9]{9}',val):
        print ("Yes")
    else:
        print ("No")

#TRYING DIFFERENCE IN SEARCH AND MATCH
l2=['99+91-9910710891',\
    '999999-9999',\
    '99999x99999']
    

for val in l2:
    if re.match(r'\+[0-9]{2}-[8-9]{1}[0-9]{9}',val):
        print ("Yes")
    else:
        print ("No")

l3=['99+91-9910710891',\
    '999999-9999',\
    '99999x99999']
    

for val in l3:
    if re.search(r'\+[0-9]{2}-[8-9]{1}[0-9]{9}',val):
        print ("Yes")
    else:
        print ("No")

re.match(r'\+[0-9]{2}-[8-9]{1}[0-9]{9}',l1[0])  #This will return address

#Task no 29
N = input("Enter a number")
if re.match(r'[\+\.-]?[0-9]*\.[0-9]+',N):
    print ("True")
else:
    print ("False")







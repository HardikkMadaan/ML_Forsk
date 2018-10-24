# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 17:39:31 2018

@author: Hardikk Madaan
"""

#data tyoes in Python....This is a single line comment

"""
This is a multi line comment.
Here it ends
First class
"""

a = None
print (type(a))

print (float(3))

number = int(input("Enter the number: "))


str1 = "Hello World"    
print (len(str1))
print (len("Welcome India"))
len(' ')
print (str1[0:5]) 
""" 5 will be excluded. Therefore printing happens from 0 to 4. This is
basically substring. known as slicing. """

print (str1[4:])
"""
Starting 4 going to end
""" 

print (str1[:7])

"""

Starting 0 going to 7
"""
print (str1)
print(str1[0:8:2])  #Skipping 2 characters
print(str1[::-1])

str1 == str1[::-1]

str2="Forsk Labs"
str3="Jaipur in MUJ"
print(str2,str3)
print(str1+'32')
print (str1.lower())
str1[0]='f' # Wont happen because str is read only

print (str2.find('Labs')) #index position form which the word is starting .If 
#If does not match then -1
print (str2.index('labs'))



str4="                Hello from Forsk"
print(str4.split('f'))

print(str4.strip())



num=20
if num==10:    #: indicates condiiton ends
    print ("Yes")
    
elif num==20:
    print("20 hain")
    
while num<30:
    print (num)
    num=num+1
    
str5="Hardikk Madaan"
"""
Output:
Madaan
Hardikk
"""
list1 = str5.split()

print (list1[1],list1[0])
index=str5.find(" ")
print(str5[index+1:],str5[:index])

print("Hello")










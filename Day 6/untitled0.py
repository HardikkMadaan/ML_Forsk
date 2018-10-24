# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:28:13 2018

@author: Hardikk Madaan
"""

import numpy as np

x = np.array([[1,2,3], [4, 5, 6]])

print (type(x))
print (x.shape)
print (type(x.shape))
print (x.dtype)

#TO CHANGE THE DATA TYPE OF VARIABLE
x = np.float32(1.0)
x = np.float64(1.0)

y=np.int_([1,2,4])
print (y)

z = np.arange(20, dtype=np.uint8)


p = np.zeros((2,3))

print (type(p.dtype))

r = np.ones((2,3) , dtype=np.uint8)

x=np.linspace(1,4,20, dtype=np.float64)

x= np.random.random((2,3))

a=np.arange(9)
print(a)

b= a.reshape(3,3)
print (b)



c=np.arange(8).reshape(2,2,2)
print (c)

np.arange(5)
np.arange(5)

print (a+b)

incomes = np.random.normal (27000, 15000, 10000)
'''First Parameter: Centered Around 27000
Second Parameter : Standard deivation of 15000
Third Paratmeter : no of values
normal distibution 
'''
np.mean(incomes)
np.median(incomes)
np.std(incomes)
np.mean(incomes)
np.median(incomes)


import matplotlib.pyplot as plot

plot.hist(incomes,20)
plot.show()


incomes = np.append(incomes , [1000000])

np.mean(incomes)
np.median(incomes)

plot.boxplot(incomes)

xs=[1,2,3,4,5]
ys=[1,2,3,4,5]
plot.plot(xs,ys)

xxs=[1.2,3,4,5]
yys=[x**3 for x in xxs]
plot.plot(xxs,yys)

xxxs=range(20)
yyys=[x**2 for x in xxxs]
plot.plot(xxxs,yyys)
plot.xlabel("x-axis")
plot.ylabel("y-axis")
plot.title("Matplotlib Example")
plot.savefig("quad.jpg")
plot.show()

x=np.arange(0,5,0.1)
y=np.sin(x)
plot.plot(x,y)

t=np.arange(0,5,0.2)
#red dashes blue squares and green cAP
plot.plot(t ,t,'r--',t, t**2,'bs',t,t**3,'g^')
plot.axis([0,6,0,150])
plot.show()

#CREATING A PIE CHART
labels = 'CSE','ECE','IT','EE'
sizes = [15,30,25,10]

plot.pie(sizes,labels=labels,autopct='%2.2f%%')
plot.axis('equal')
plot.show()











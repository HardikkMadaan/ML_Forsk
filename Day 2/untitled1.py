# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 17:27:07 2018

@author: Hardikk Madaan
"""

a = "Hello World"
type(a)
len(a)

for item in a:
    print(item)    
    
    #This is for loop in python .Item is just a name it can be anything such as xy z anything
              
num=10
while num < 30:
    if num%2==0:
        pass
    else:
        print(num)
    num=num+1
    #LISTS ARE ARRAYS OF PYTHON
list1 = [1,2,3,4,5,6,7]    #LIST IS MUTABLE.THAT MEANS IT CAN BE MODIFIED
type(list1)

print (list1[0])
len(list1)

list1.insert(3,71)
list1.append(14)
list1.append([15,16])
list1.insert(1,34)
list1[0]=79
list1.sort()    #in place sorting
list1.reverse()   #to reverse a list
list1.remove(34) # USED TO REMOVE THE VALUE PASSED AS ARGUEMENT

if 34 in list1:
    print("Yes")
    list1.remove(34)
else:
    print ("Item not found")

list1.index(3)
list1.index(14)
list1.pop()
list2=[30,40,50]
list1.append(list2)
print (list1[7])
print (list1[10][1])
list1.extend(list2)
for item in list2:
    list1.append(item)

del list2[2]  #DELETE IS A UNIVERSAL FUNCTION

list3=[1,2,3,2,2,3,5,6]
for item in list3:
    list3.remove(2)

for item in list3:
    if item ==2:
        list3.remove(2)
        
while 2 in list3:
    list3.remove(2)
    

# DEFINING A FUNCTION
def add2(a,b):                 #IN THIS CASE THE FUNCTION PRINTS THE VALUE
    print  (a+b)         #AFTER THAT IT RETURNS NOTHING .THEREFORE NONE ALSO COMES

print (add2(4,5))


def add1(a,b):        #IN THIS CASE ONLY THE ANSWER IS PRINTED BECAUSE THAT IS WHAT
    return a+b          #IS RETURNED TO PRINT
print (add1(7,8))

def add(a,b=10):    #DEFAULT VALUE IS PASSED IN THIS FUNCTION AS ARGUEMENT
    return a+b
print (add(4))
print (add(4,5))   #IN THIS CASE AS BOTH PARA ARE PASSED.THEREFORE DEAULT VALUE IS NOT USED


def add3(a=10,b):  #THIS WILL SHOW ERROR BECUASE DEFAULT ARGS COME IN THE END
                     #SyntaxError: non-default argument follows default argument
    return a+b


def add5(a,b): 
    #IN THIS CASE WE WILL EXPLICITLY MENTION THE VALUES THEREFORE ORDER 
    """All these comments are doc strings meaning they are documented strings and will not
get printed"""
    return a+b     #WILL NOT REALLY MATTER
print (add(b=4,a=5))

print (add5.__doc__)


a=[1,2]
b=[1,2]

a==b     #THIS CHECKS FOR THE VALUES IN A AND B
a is b       #BECAUSE THEIR MEMORY ADDRESS IS DIFFERENT  .ASNWER IS FALSE
c=a
a is c    #BECAUSE WE HAVE ALREADY DEFINED THAT C IS EQUAL TO A

def f(x):
    return x % 3 ==0

print (f(6))

list1=list(range(2,25))


list(filter (f,list1))    #TAKES TWO ARGS FIRST IS FUNCION NAME SECOND IS VARIABLE NAME
def cube(x):
    return x**3

list(map(cube,[1,2,3,4,5]))

def adde(x,y):
    return x+y
    
functools.reduce(adde, [1,2,3,4,5])


tuple1 = (1,2,3,4,5)  #TUPLES CANNOT BE MODIFIED


divmod(34,5)   #SHOWS THE QUOTIENT AND REMAINDER
q,r=divmod(34,5)   #THIS CONCEPT IS CALLED UNPACKING OF THE DATA


x=(3,)    #TO USE SINGLE VALUE AS A TUPLE .WE USE A COMMA(,)
type(x)


# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:32:04 2018

@author: Hardikk Madaan
"""

import pandas as pd

#READ CSV FILE
df= pd.read_csv("Salaries.csv")

#LIST FIRST 10 RECORDS
df.head(10)
df.head()     # leaving it blank will give first five records as the default value is 5
df.tail()  #GIVES LAST 5 RECORDS
df.tail(900)

'''
String or text data will come as object
Also alphanumeric data will come as object
'''
'''
nan means not a number or a missing value
'''
#Check types for all the columns
df.dtypes
df.columns #list the column names
df.axes #list the row labelsand column names
df.ndim   #number of dimensions
df.size #number of elements
df.shape #return a tuple representing the dimensionality
df.values #numpyrepresentation of the data

df.describe() #generate descriptive statistics (for numeric columns only)

df.max() #return max/minvalues for all numeric columns
df.min()

df.mean()
df.median()
df.std()

df.sample(10) #returns a random sample of thedata frame

#What are the mean values of the first 50 records in the dataset?
df.head(5).mean()

"""
Selecting a column in a Data Frame
Method 1: Subset the data frame using column name:
df['sex']
Method 2: Use the column name as an attribute:
df.sex
Note:there is an attribute rankfor pandas data frames, 
so to select a column with a name "rank" we should use method 1.
"""

df['phd']
df.phd

df['rank']
df['rank'].value_counts()
df['rank'].value_counts(normalize = True)

#calculate the basic statstics on the salary column
df['salary'].mean()
df['salary'].describe()

#Find how many values in the salarycolumn (use countmethod);
df['salary'].count()

#calculate the avg salary
print (df['salary'].mean())


"""
Data Frame: filtering
29
To subset the data we can apply Boolean indexing. 
This indexing is commonly known as a filter. 
For example if we want to subset the rows in which the salary
 value is greater than $120K:
"""
#Calculate mean salary for each professor rank:
df_sub= df[df['salary'] > 120000 ]
df_sub =df[(df['salary'] > 120000) &\
            (df['phd'] > 10 ) & \
             (df['sex'] == 'Female')]

#Select only those rows that contain female professors:
df_f= df[df['sex'] == 'Female' ]

S1= df[df['sex']=='Female']['salary']
DF1 = pd.DataFrame(S1)

type(S1)

type(DF1)

df[['rank','salary']]

"""
Data Frames: method loc
33
If we need to select a range of rows, using their labels 
we can use method loc
"""
df.loc[10:15,['rank','sex']]
df.loc[10:]


"""
Data Frames: method iloc

If we need to select a range of rows and/or columns, 
using their positions we can use method iloc
"""
df.iloc[2:10,[0,2,3]]

df.iloc[0] # First row of a data frame

df.iloc[1:5, :-1]   #LEAVE LAST COLUMN

df.iloc[-1] # Last row

df.iloc[:, 0] # First column

df.iloc[:, -1] # Last column

df.iloc[0:7] #First 7 rows

df.iloc[:, 0:2] #First 2 columns

df.iloc[1:3, 0:2] #Second through third rows and first 2 columns

df.iloc[[0,5], [1,3]] #1stand 6throws and 2ndand 4thcolumns


import pandas as pd
salary = pd.read_csv("Salaries.csv")

#RETURN A MATRIX BY CHECKING INDIVIDUAL VALUE. GIVES TRUE IF VALUE IS NULL
salary.isnull()
#CHECKS IF A NULL VALUE IS THERE IN A COLUMN
salary.isnull().any(axis=0)
#OR
salary.isnull().any
#CHECKS IF A NULL VALUE IS THERE IN A ROW
salary.isnull().any(axis=1)
#RETURN THE DETAILS OF THE PLACE WHERE MISSING VALUES ARE PRESENT

salary[salary.isnull().any(axis=1)]

salary[salary.isnull().any(axis=1)].head(2)
''' gives the first two rows of the missing data'''

''' dropna will delete all the rows wiht any missing values in that row'''

new_df = salary.dropna()
new_df[new_df.isnull().any(axis=1)]


"""
dropna(how='all') >> Drop observations where all cells is NA
dropna(axis=1, how='all') >> Drop column if all the values aremissing
dropna(thresh = 5) >> Drop rows that contain less than 5 non-missing values
fillna(0) >> Replace missing values with zeros
isnull() >> returns True if the value is missing
notnull() >> Returns True for non-missing values

More notes:
    Missing Values

•When summing the data, missing values will be treated as zero
•If all values are missing, the sum will be equal to NaN
•cumsum() and cumprod() methods ignore missing values but 
preserve them in the resulting arrays
•Missing values in GroupBymethod are excluded (just like in R)
•Many descriptive statistics methods have skipnaoption to control 
if missing data should be excluded . This value is set to True by 
default (unlike R)

"""
salary = pd.read_csv("Salaries.csv")
#FILLING ALL THE MISSING RECORDS IN THE PHD COLUMN
salary['phd'] = salary['phd'].fillna(salary['phd'].mean())

#All columns
salary = salary.fillna(salary.mean())









import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



### Problem 1 ####

val = -3
n = 5
series = pd.Series(val,index=range(2,12,2))

dct = {'Bill': 31, 'Sarah':28, 'Jane': 34, 'Joe': 26}
Data = pd.Series(dct)
print series, Data


### Problem 2 ###### 

N = 1000
for i in xrange(5):
    s = np.zeros(N)
    s[1:] = np.random.binomial(1, .5, size=(N-1,))*2-1
    s = pd.Series(s)
    s = s.cumsum()
    s.plot()
    plt.ylim([-50,50])

plt.show()

N=100
s = np.zeros(N)
s[1:] = np.random.binomial(1, .51,size =(N-1,))*2-1
s = pd.Series(s)
s=s.cumsum()
s.plot()
plt.ylim([-1000,1000])

plt.show()



N=10000
s = np.zeros(N)
s[1:] = np.random.binomial(1, .51, size=(N-1,))*2-1
s = pd.Series(s)
s = s.cumsum()
s.plot()
plt.ylim([-1000,1000])

plt.show()

N=100000
s = np.zeros(100000)
s[1:] = np.random.binomial(1, .51, size=(N-1,))*2-1
s = pd.Series(s)
s = s.cumsum()
s.plot()
plt.ylim([-1000,1000])

plt.show()



### Problem 3 ####

name = ['Bill', 'Alice', 'Joe', 'Jenny', 'Ted', 
    'Taylor', 'Tracy', 'Morgan','Liz']
sex = ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'F']
age = [20, 21, 18, 22, 19, 20, 20, 19, 20]
rank = ['Sp', 'Se', 'Fr', 'Se', 'Sp', 'J', 'J', 'J', 'Se']
ID = range(9)
aid = ['y', 'n', 'n', 'y', 'n', 'n', 'n', 'y', 'n']
GPA = [3.8, 3.5, 3.0, 3.9, 2.8, 2.9, 3.8, 3.4, 3.7]
mathID = [0, 1, 5, 6, 3]
mathGd = [4.0, 3.0, 3.5, 3.0, 4.0]
major = ['y', 'n', 'y', 'n', 'n']
studentInfo = pd.DataFrame({'ID': ID, 'Name': name,
    'Sex': sex, 'Age': age, 'Class': rank})
otherInfo = pd.DataFrame({'ID': ID, 'GPA': GPA, 
    'Financial_Aid': aid})
mathInfo = pd.DataFrame({'ID': mathID, 'Grade': mathGd, 
    'Math_Major': major})

#SELECT ID, Name from studentInfo WHERE Age > 19 AND Sex ='M'

print studentInfo[(studentInfo['Sex'] == 'M')&(studentInfo['Age']>19)][["ID",'Name']]

## Problem 4 ##

splits = otherInfo.merge(studentInfo[studentInfo['Sex']=='M'], 
        on= 'ID')[['Age','GPA','ID']]

## Problem 5 ## 

crime_data = pd.read_csv("crime_copy.csv", index_col=0)
crime_data['Crimesperyear']=crime_data['Total']/crime_data['Population']
crimeseries = pd.Series(crime_data['Crimesperyear'])

plt.title("Crime Rate")
crimeseries.plot()

plt.show()

print crime_data.sort(columns = 'Crimesperyear', 
        ascending = False).head(5)

average = crime_data.mean()
print 'Average Total Crimes committed', average[1]
print 'Average Beurglary Crimes committed', average[8]

print crime_data[(crime_data['Total']>average[1]) 
        & (crime_data['Burglary']<average[8])]

x_data = pd.Series(crime_data['Murder'])
y_data = pd.Series(crime_data['Population'])
plt.title('Murders Plotted Against the Total Population')
plt.plot(y_data,x_data)
plt.show()

subcrime_data = crime_data[(crime_data.index>=1980) & (crime_data.index<1990)][['Population', 'Violent', 'Robbery']]

subcrime_data.to_csv('SmallerCrimeData.csv')



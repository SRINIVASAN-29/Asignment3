import numpy as np
import pandas as pd



#asignment1 day3
l1 = [1,2,3,4,5]
l2 = [2,3,4,5,6]
l3 = [4,5,6,7,8]

arr=np.array([l1,l2,l3])
print(arr[1:,2:])

#Create a dataframe using np.random.randn function with 5 rows and 4 columns, and performs various operations using pandas library
arr=np.arange(0,20).reshape(4,5)
print('\n',arr)

df=pd.DataFrame(np.random.rand(5,4),index=['a','b','c','d','f'],columns=['one','two','three','four'])
print('\n',df.head())
print('\n',df['one'])
print('\nthe loc:\n',df.loc['a'])
print('\nthe loc of r1c1:\n',df.loc['a','one'])
print('\nthe iloc:\n', df.iloc[0:2,1:3])
print('\n',df.info)
print('\n',df.describe())
print('\n',df.nunique())





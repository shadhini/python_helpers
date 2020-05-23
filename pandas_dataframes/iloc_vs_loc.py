import pandas as pd
import numpy as np

students = [ ('jack', 34, 'Sydeny') ,
('Riti', 30, 'Delhi' ) ,
('Aadi', 16, 'New York'),
(np.nan, 16, 'New York'),
('Tada', -99999.000, 'New York')]
# Create a DataFrame object
dfObj = pd.DataFrame(students, columns = ['Name' , 'Age', 'City'], index=['a', 'b', 'c', 'd', 'e'])

print(dfObj)


################################################
# DataFrame.loc | Select Column & Rows by Name #
################################################

columnsData = dfObj.loc[ : , ['Age', 'Name'] ]
rowData = dfObj.loc['b', :]
subset = dfObj.loc[ ['c' , 'b'] ,['Age', 'Name'] ]

#################################################################
# DataFrame.iloc | Select Column Indexes & Rows Index Positions #
#################################################################


print(dfObj.iloc[:, [0, 2]])
print(dfObj.iloc[ 0:2 , : ])
print(	dfObj.iloc[[0 , 2] , [1 , 2] ])
print(dfObj.iloc[ 0:2 , 0:2 ])


################

print(dfObj.iloc[-2, 0])
print(dfObj.iloc[-1, 1])
if np.isnan(dfObj.iloc[-2, 0]):
    dfObj.iloc[-2, 0] = 0
if dfObj.iloc[-1, 1] < 0:
    dfObj.iloc[-1, 1] = 0

print(dfObj)




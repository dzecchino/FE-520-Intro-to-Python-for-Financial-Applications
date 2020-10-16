from pandas import Series, DataFrame, ExcelWriter, ExcelFile
import pandas as pd
import numpy as np
import math

#df = pd.read_excel(open('/home/dominic/Documents/Python/FE 520/HW4/Homework4_Dataset/Energy.xlsx', 'rb'), sheetname = 'Sheet1')        #didnt work
BalanceSheet = pd.read_excel (r'/home/dominic/Documents/Python/FE 520/HW4/Homework4_Dataset/Energy.xlsx')                               #works
Ratings = pd.read_excel (r'/home/dominic/Documents/Python/FE 520/HW4/Homework4_Dataset/EnergyRating.xlsx')                              #works
frame1  = pd.DataFrame(BalanceSheet)
frame1copy = frame1

rows = len(frame1)
column = len(frame1.columns)
temp = range(column)

#print(frame1.dtypes)

for i in temp:
    if (not(frame1.dtypes[i] == np.int64 or frame1.dtypes[i] == np.float64)):
        frame1copy = frame1.drop(frame1.columns[i], 1)
        #temp = range(len(frame1.columns))                          #don work

print(frame1copy)


#frame1 = frame1.T                      #probably not the way i should do this
#print (data)
#print (data2)

count = 0
for j in range(column):
    frame2 = frame1.columns[j]
    print(frame2)
    print()
    #=============This is for the first column that needs testing

    for i in range(rows):
        x = frame1.iloc[i][frame2]
        if(x == None or float(x) == 0.0 ):
            count += 1
            print(count)

        if ((count/rows) > 0.9 ):
            frame1 = frame1.drop(frame2, axis=1)

print(frame1)

#    for i in range(rows):
#        #x = float(frame1[i+1])
#        if(is_number(frame1[i])):#or frame1[i] == None or int(frame1[i]) == 0 ):
#            count += 1
#        if ((count/rows) > 0.9 ):
#            frame1copy.drop(frame1.columns[j])
#            frame1copy = frame1copy.drop(frame1copy.columns[j])


print('count is: ',count)
#print(len(frame1))                     #test Code
#print(frame1)                          #test Code
#print(frame1['Global Company Key'])    #test Code
#print(frame1.columns[1])               #test code
#print(len(frame1.columns))             #test code

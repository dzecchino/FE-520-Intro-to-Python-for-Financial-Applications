from pandas import Series, DataFrame
import pandas as pd
import numpy as np


#class CSVFile:

data = pd.read_csv (r'/home/dominic/Documents/Python/FE 520/HW4/Homework4_Dataset/res_purchase_2014.csv')
table = pd.DataFrame(data, columns= ['Year-Month','Agency Number','Agency Name','Cardholder Last Name','Cardholder First Initial','Description','Amount','Vendor','Transaction Date','Posted Date','Merchant Category Code (MCC)'])

def clean(s):
    res = ""
    for i in str(s):
        if (i is "-"):
            res += i
        if (i is "."):
            res += i
        if (i.isdigit()):
            res += i
    return res
table['Amount'] = table['Amount'].map(clean)
#table['Amount'] = table['Amount'].str.extract('^(\d*\.*\d*)', expand=False)                 #looking to map instead
#table['Amount'] = table['Amount']str.replace(r"[a-zA-Z],'')
#table['Amount'] = table['Amount'].map(lambda x: ''.join([i for i in x if i.isdigit()]))
#table['Amount'] = table['Amount'].astype(float)

#print(table['Amount'])
#def WWGrainger():

    #print (table)                          #This shows that I am properly reading the data
    #print (table.iloc[0]['Description'])           #Testing to see if the columns are properly set
    #print(len(table))                      #Shows me that I do not need to search for the number of rows specifically, and that it is automatic

    #frame = pd.DataFrame(table)
    #print(frame)

    #print(table.iloc[0]['Vendor'])         #Testing to retrieve specific values from a given row of a data set

    #print(table.iloc[50]['Vendor'])        #Index 50 is the first known location of WW Grainer

totalSpent = 0
SpentWWG = 0
SpentGS = 0
SpentWMS = 0
'''
temp = ''
sum = 0.0
for i in range (len(table)):
  amount = table.iloc[i]['Amount']
  count = 0
  print(i)
  for j in range (len(table.iloc[i]['Amount'])):
    temp = 0
    if(amount[j] != 1 or amount[j] != 2 or amount[j] != 3 or amount[j] != 4 or amount[j] != 5 or amount[j] != 6 or amount[j] != 7 or amount[j] != 8 or amount[j] != 9 or amount[j] != 0 or i != '.'):
        temp = 0
    else:
        temp = float(amount[i])
    sum+= temp


print(sum)

'''
#x=table.iloc[50]['Vendor']
#y=table.iloc[265463]['Vendor']
#z= table.iloc[265543]['Merchant Category Code (MCC)']
#print(x,y,z)
x = "WW GRAINGER"
y = "WM SUPERCENTER"
z = "GROCERY STORES,AND SUPERMARKETS"
print("Please be patient, the code isn't optimized so it takes a few minutes.")
for i in range (len(table)):
#        '''=====================The code below is for total spending======================='''
    #print(i)
    #table.iloc[i]['Amount'] = table.iloc[i]['Amount'].str.extract('(\d+)', expand=False)           #determined there is probably a better way to do this
    amount = float(table.iloc[i]['Amount'])
    #amount = round(amount, 2)                      #not useful anymore
    #print('The amount is===== ', amount)
    totalSpent = round(totalSpent + amount, 2)


#    '''=====================The code below is for WW Grainger======================='''
                                                #Used to test the total amount
    #if (table.iloc[i]['Vendor'] == "WW GRAINER")                       #First attempt at getting the correct amounts
    if (x in table.iloc[i]['Vendor']):           #For now i will resort to this method until I can come up with a better one
        value = table.iloc[i]['Amount']
        #print(value)
        #value = int(value)                                             #This is the wrong typecast, it should be float
        SpentWWG = SpentWWG + float(value)                              #This should be the proper formula
        SpentWWG = round(SpentWWG, 2)                                   #Without this rounding the answer doesnt come out to 2 decimal places for some reason
        #print(f'The concatenated spending value is {SpentWWG:.2f}')
        #SpentWWG = {SpentWWG:.2f}                                      #not the right method
        #print('The current value being examined is: ',value)           #Print statement used to test
        #print('The total amount spent at WW GRAINGER is: ', SpentWWG)               #Print statement used to test
        #print('''================================================================================================================================================================
        #    ================================================================================================================================================================
        #    ================================================================================================================================================================
        #    ''')
    #print(i)                                                       #Print statement used to test

#   ===================== The code below is for WM Supercenter ====================
    if (y in table.iloc[i]['Vendor']):           #For now i will resort to this method until I can come up with a better one
        #print(i)
        value = table.iloc[i]['Amount']
      #value = int(value)                                             #This is the wrong typecast, it should be float
        SpentWMS = SpentWMS + float(value)                              #This should be the proper formula
        SpentWMS = round(SpentWMS, 2)


#   ====================== The code below is for Grocery Stores =====================
    if (z in table.iloc[i]['Merchant Category Code (MCC)']):           #For now i will resort to this method until I can come up with a better one
        #print(i)
        value = table.iloc[i]['Amount']
      #value = int(value)                                             #This is the wrong typecast, it should be float
        SpentGS = SpentGS + float(value)                              #This should be the proper formula
        SpentGS = round(SpentGS, 2)
#   ====================== The code below outputs our desired values =====================
print('The total amount spent overall is: ',totalSpent)
print('The amount spent at WW GRAINGER is: ', SpentWWG)
print('The amount spent at WM Supercenter is: ', SpentWMS)
print('The amount spent at the Grocery Stores is: ', SpentGS)



#print(table.iloc[265446]['Vendor'])                                  #used for testing

'''
if __name__ == "__main__":
    csv = CSVFile()
    csv.WWGrainger()
'''

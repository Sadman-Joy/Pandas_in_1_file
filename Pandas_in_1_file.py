import pandas as pd
# For excel file install - openpyxl


 # Selfmade data :
 #-----------------

'''
mydata = {"Name" : ["Joy","Mahamudul","Noman"],
         "Age" : [25,25,25],
         "Salary" : [50000,55000,58000]
         }

df = pd.DataFrame(mydata)
print(df)

'''

 # Work with excel file & overview the whole data
 #------------------------------------------------

'''
data = pd.read_excel("ESD.xlsx")
#print(data)

# Display first 10 datas :
print(data.head(10))

# Display last 10 datas :
print(data.tail(10))

# Show the files information :
print(data.info())

# Some built-in calculation : 
print(data.describe())

'''


 # Data Cleaning 
 #---------------------

'''
data1 = pd.read_csv("company1.csv") # data1 is the first variable

# First delete/drop unnecessary columns :
data2 = data1.drop(columns=["Benefits","Extra"]) 
# data2 is the new variable with deleted unnecessary column


# Check duplicates :
# Always check the ID column cz ID column is the primary column 
data2["EEID"].duplicated().sum()

data3 = data2.drop_duplicates("EEID") # So delete the duplicates
#data3 is new variable with deleted the duplicates

# Check null values :
# print(data3.isnull().sum())

# Fill null values

import numpy as np

# Best way to fill null values with the mean of the column:
# print(data3["salary"].mean())

data3["salary"] = data3["salary"].replace(np.nan, 25666)
'''

 # Column transformation 
 #-----------------------
'''
d1 = pd.read_excel("ESD.xlsx")
d1.loc[(d1["Bonus %"]==0), "GetBonus"] = "no bonus"
d1.loc[(d1["Bonus %"] > 0), "GetBonus"] = "bonus"
print(d1.head(10))

'''

 # Groupwise query 
 #-----------------

'''
d1 = pd.read_excel("ESD.xlsx")

short = d1.groupby(["Full Name","Department"]).agg({"Annual Salary":"mean"})
print(short)

'''

 # Merge, concatenate
 #--------------------

'''
mydt1 = {"Id" : [101,102,103],
         "Name" : ["Joy","Mahamudul","Noman"],
         "Age" : [25,25,25]
        }

mydt2 = {"Id" : [101,102,103],
         "Salary" : [50000,55000,58000]
         }

mydt3 = {"Id" : [104,105,106],
         "Name" : ["Yoj","Ludumaham","Namon"],
         "Age" : [26,26,26]
        }

dt1 = pd.DataFrame(mydt1)
dt2 = pd.DataFrame(mydt2)
dt3 = pd.DataFrame(mydt3)

merged = pd.merge(dt1,dt2, on = "Id" )
# Now merged is the new-merged variable

# Combine :
both = pd.concat([dt1,dt3])

'''
# Compare :
'''
products1 = {
    "Name" : ["Lichi","Mango","Grapes"],
    "Quantity" : [100,10,50],
    "Price" : [200,300,500]
}

products2 = {
    "Name" : ["Lichi","Mango","Grapes"],
    "Quantity" : [100,10,50],
    "Price" : [250,350,500]
}

prd1 = pd.DataFrame(products1)
prd2 = pd.DataFrame(products2)

print(prd1.compare(prd2))

'''
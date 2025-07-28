# Databricks notebook source
python is interpreted language code executed line by line.In java we have to compile and execute.

#Variable in python 

its dynamic languge its infer the datatype in runtime



# COMMAND ----------

insurane_type = "medicaid"
income = None
insurane_rate = 763.90
insurane_rate_new = '763.90'
is_start_date = True
print(type(insurane_type))
print(type(income))
print(type(insurane_rate))
print(type(is_start_date))
print(type(insurane_rate_new))

fees = int(insurane_rate) #+ (int(insurane_rate_new))
print(fees)

# COMMAND ----------

#can we add float and string
print(insurane_rate + 500)

#we can concat with string and int?
#yes we can But can't add

# COMMAND ----------

#inbigdata engineering we have to load the file in sting only.Normally if we want to other language we haave deffine the datatypes first. but in python it weill do itself



# COMMAND ----------

#stirng concat
fname ="sug"
lname = "bala"
print(fname+" "+lname)

# COMMAND ----------

import math
total_sale = 2000.60
total_sale1 = -2000.60
print(math.ceil(total_sale))
print(math.floor(total_sale))
print(math.fabs(total_sale1))
print(math.ceil(total_sale1))
print(math.floor(total_sale1))


# COMMAND ----------

math.

# COMMAND ----------

#conditional statements
marks = int(input("enter marks : "))

# COMMAND ----------

\t  is tab
\n print in new line
escape characters

# COMMAND ----------

name ="sug"
print(len(name))

# COMMAND ----------

#indexing -helps to get a particular character - strats from 0.srting are immutable , we cannot make any changes.if we want to chane create a new string in df and do it.

# slicing -- helps to get slice

#indexing 

order_status = "complete order"
print(order_status[1])
print(order_status[-1])
print(order_status[12])


# slicing 
print(order_status[0:8])
print(order_status[9:14])
print(order_status[9:len(order_status)])
length = len(order_status)
print(order_status[9:length])
print(order_status[:8])
print(order_status[:])
print(order_status[-5:])
print(order_status[-5:len(order_status)])

#print after the space
index =order_status.find(" ")

print(order_status[index:])
print(order_status[index+1:])
print(order_status[index+1:])

# index =order_status.get(" ")
# print(index)

#print after the space
print(order_status[0:index])

# COMMAND ----------


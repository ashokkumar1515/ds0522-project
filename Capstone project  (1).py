#!/usr/bin/env python
# coding: utf-8

# # PHASE-1

# In[1]:


# LINK :- https://www.findeasy.in/top-indian-states-by-population/
# https://simple.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area
# https://www.kaggle.com/datasets/doncorleone92/govt-of-india-literacy-rate
# https://ncrb.gov.in/sites/default/files/crime_in_india_table_additional_table_chapter_reports/Table%201.9_2010.pdf


# Data which is given below taken by above links
importing necessary library
# In[2]:


import pandas as pd
import numpy as np


# # Literacy Rate and population in each state

# In[3]:


df1=pd.read_excel(r"C:\Users\hp\OneDrive\Desktop\LITERACY.xlsx")


# In[4]:


df1


# # Area of each state

# In[5]:


df2=pd.read_excel(r"C:\Users\hp\OneDrive\Desktop\Book121.xlsx")


# In[6]:


df2


# # Crime report

# In[7]:


df3=pd.read_excel(r"C:\Users\hp\OneDrive\Desktop\wapasBook1.xlsx")


# In[8]:


df3


# In[9]:


df4=pd.concat([df1,df2,df3],axis=1)


# In[10]:


df4


# In[11]:


df4.drop(['State Name_UT','S.No.'],axis=1,inplace=True)


# # new file

# In[12]:


df4


# # PHASE-2

# In[13]:


import pandas as pd
import numpy as np


# In[14]:


df4


# check the shape of file

# In[15]:


df4.shape


# check the information of file

# In[16]:


df4.info()


# check the null values in file

# In[17]:


df4.isnull().sum()


# # Making DataFrame for the Nominal Data

# In[18]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[19]:


sns.scatterplot(x='Literacy Rate',y='Total Crime',data=df4)


# it is seen that where literacy rate is low crime rate high.

# In[20]:


sns.scatterplot(x='Area (km2)',y='Total Crime',data=df4)


# it is seen that where Area is increase crime rate also increase.

# In[21]:


sns.scatterplot(x='Population',y='Total Crime',data=df4)


#  it is seen that where Population is more crime rate also more.

# In[22]:


df5=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\India_Crime - Copy\01_District_wise_crimes_committed_IPC_2001_2012.csv")


# In[23]:


df5


# In[24]:


sns.scatterplot(x='YEAR',y='TOTAL IPC CRIMES',data=df5)


# it is seen that whereYear is increase crime rate also increase.

# # Each state crime report

# It is seen that day by day crime increse.In other word that as well as time increase crime also increase.The main reason of increase crime according to me is illiteracy.One other factor to increase crime is increasing Population.

# State Name_UT                      and                              Total Crime
# Andaman & Nicobar Island                                              119
# ANDHRA PRADESH                                                        67561
# ARUNACHAL PRADESH                                                     724
# ASSAM                                                                 13541
# BIHAR                                                                 31238
# CHANDIGARH                                                            169
# CHHATTISGARH                                                          15305
# Dadra and Nagar Haveli                                                56
# DAMAN & DIU                                                           60
# DELHI                                                                 6994
# GOA                                                                   523
# GUJARAT                                                               19039
# HARYANA                                                               8195
# HIMACHAL PRADESH                                                      2396
# JAMMU & KASHMIR                                                       2622
# JHARKHAND                                                             9793
# KARNATAKA                                                             27429
# KERALA                                                                19650
# LAKSHADWEEP                                                           1
# MADHYA PRADESH                                                        52241
# MAHARASHTRA                                                           49534
# MANIPUR                                                               778
# MEGHALAYA                                                             480
# MIZORAM                                                               251
# NAGALAND                                                              201
# ODISHA                                                                14422
# PUDUCHERRY                                                            1133
# PUNJAB                                                                11033
# RAJASTHAN                                                             33292
# SIKKIM                                                                151
# TAMIL NADU                                                            42221
# Telangana                                                             936
# TRIPURA                                                               1708
# UTTAR PRADESH                                                         40935
# UTTARAKHAND                                                           2453
# WEST BENGAL                                                           24095

# #                                             PHASE-3

#                             IMPORT SQLITE3 AND MAKE CONNECTION THEM

# In[25]:


import sqlite3
db=sqlite3.connect("District_wise_crimes_committed_against_women_2001_2012.db")
cursor=db.cursor()


# # 3.1Insert records from 42_District_wise_crimes_committed_against_women_2001_2012.csv into a table

#                                         CREATE TABLE 

# In[26]:


cursor.execute("CREATE TABLE crimes_on_women (STATE_UT TEXT,DISTRICT TEXT,Year INT,Rape INT,Kidnapping_and_Abduction INT,Dowry Deaths INT,Assault_on_ women with intent_to_outrage her modesty INT,Insult_to_modesty_of_Women INT,Cruelty_by_Husband_or_his Relatives INT,Importation_of_Girls INT)")


#                              INSERT DATA FROM CSV FILE District_wise_crimes_committed_against_women_2001_2012

# In[27]:


with open(r"C:\Users\hp\OneDrive\Desktop\India_Crime - Copy\42_District_wise_crimes_committed_against_women_2001_2012.csv") as file :
    no_records=0
    for row in file:
        cursor.execute("INSERT INTO crimes_on_women VALUES (?,?,?,?,?,?,?,?,?,?)" ,row.split(","))
        db.commit()
        no_records+=1
print(no_records , 'inserted')
    


#                                    VARIFY DATA INSERT OR NOT

# In[28]:


sql = "select * from crimes_on_women "
results =  cursor.execute(sql)
for row in results:
    print(row)


# #  3.2	 SQL query to find the highest number of rapes & Kidnappings that happened in which state, District, and year

# In[29]:


results = cursor.execute("SELECT MIN(Rape) FROM crimes_on_women")
print('Minimum Rape = ',results.fetchone())


# In[30]:


results = cursor.execute("SELECT MAX(Rape) FROM crimes_on_women")
print('Maximum Rape = ',results.fetchone())


# In[31]:


results = cursor.execute("SELECT MIN(Kidnapping_and_Abduction) FROM crimes_on_women")
print('Minimum Kidnapping_and_Abduction = ',results.fetchone())


# In[32]:


results = cursor.execute("SELECT MAX(Kidnapping_and_Abduction) FROM crimes_on_women")
print('Maximum Kidnapping_and_Abduction = ',results.fetchone())


# In[33]:


Max = "SELECT * FROM crimes_on_women ORDER BY Rape desc"
results = cursor.execute(Max)
for row in results:
    print(row)


# In[34]:


Max = "SELECT * FROM crimes_on_women ORDER BY Kidnapping_and_Abduction desc"
results = cursor.execute(Max)
for row in results:
    print(row)


# # 3.3 SQL query to find All the lowest number of rapes & Kidnappings that happened in which state, District, and year

# In[35]:


Min = "SELECT * FROM crimes_on_women ORDER BY Rape "
results = cursor.execute(Min)
for row in results:
    print(row)


# In[36]:


Min = "SELECT * FROM crimes_on_women ORDER BY Kidnapping_and_Abduction "
results = cursor.execute(Min)
for row in results:
    print(row)


# In[37]:


DESC = "SELECT * FROM crimes_on_women ORDER BY Kidnapping_and_Abduction  "
results = cursor.execute(DESC)
for row in results:
    print(row)


# In[ ]:





# #                        3.4	Insert records from 02_District_wise_crimes_committed_against_ST_2001_2012.csv into a new table

#                                     create table

# In[38]:


cursor.execute("create table  crimes_against_ST(STATE_UT TEXT,DISTRICT TEXT,Year INT,Murder INT,Rape INT,Kidnapping Abduction INT,Dacoity INT,Robbery INT,Arson INT,Hurt INT,Protection of Civil Rights_PCR_Act INT,Prevention of atrocities_POA_Act INT,Other Crimes Against STs INT)")


# In[39]:


with open (r"C:\Users\hp\OneDrive\Desktop\India_Crime - Copy\02_District_wise_crimes_committed_against_ST_2001_2012.csv") as file:
    no_record=0
    for row in file:
        cursor.execute("INSERT INTO crimes_against_ST VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",row.split(",") )
        db.commit()
        no_record+=1
    print(no_record ,'inserted')


#                              check data inserted or not

# In[40]:


sql="select * from crimes_against_ST "
results=cursor.execute(sql)
for row in results:
    print(row)


# # 3.5 SQL query to find the highest number of dacoity/robbery in which district.

# In[41]:


Max = "SELECT * FROM crimes_against_ST order BY  Dacoity desc "
results = cursor.execute(Max)
for row in results:
    print(row)


# In[42]:


Max = "SELECT * FROM crimes_against_ST order BY Robbery desc "
results = cursor.execute(Max)
for row in results:
    print(row)


# #                      3.6 SQL query to find in which districts(All) the lowest number of murders happened.

# In[43]:


Max = "SELECT * FROM crimes_against_ST order BY Murder "
results = cursor.execute(Max)
for row in results:
    print(row)


# # 3.7	 SQL query to find the number of murders in ascending order in district and yearwise.

# In[44]:


DESC = "SELECT * FROM crimes_against_ST order BY Murder  desc"
results = cursor.execute(DESC)
for row in results:
    print(row)


# # 3.8.1 Insert records of STATE/UT, DISTRICT, YEAR, MURDER, ATTEMPT TO MURDER, and RAPE columns only from 

# In[45]:


cursor.execute("create table crimes_committed_IPC(STATE_UT text, DISTRICT int, YEAR int, MURDER int, ATTEMPT_TO_MURDER int,RAPE int)")


# In[46]:


with open (r"C:\Users\hp\OneDrive\Desktop\New folder (2)\01_District_wise_crimes_committed_IPC_2001_2012.csv") as file:
    no_record=0
    for row in file:
        cursor.execute("INSERT INTO crimes_committed_IPC VALUES (?,?,?,?,?,?)",row.split(",") )
        db.commit()
        no_record+=1
    print(no_record ,'inserted')


#  check data inserted or not

# In[47]:


sql = "select * from crimes_committed_IPC "
results =  cursor.execute(sql)
for row in results:
    print(row)


# # 3.8.2	SQL query to find which District in each state/ut has the highest number of murders yearwise. Your output should show STATE/UT, YEAR, DISTRICT, and MURDERS.

# In[48]:


Max = "SELECT * FROM crimes_committed_IPC order BY Murder "
results = cursor.execute(Max)
for row in results:
    print(row)


# In[ ]:





# # PHSAE-4

# In[49]:


import pandas as pd
import numpy as np


# In[50]:


df1=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\India_Crime - Copy\03_District_wise_crimes_committed_against_children_2001_2012.csv")


# In[51]:


df2=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\India_Crime - Copy\02_District_wise_crimes_committed_against_ST_2001_2012.csv")


# In[52]:


df3=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\India_Crime - Copy\02_01_District_wise_crimes_committed_against_SC_2001_2012.csv")


# In[53]:


df4=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\India_Crime - Copy\01_District_wise_crimes_committed_IPC_2001_2012.csv")


# In[54]:


df5=pd.merge(df1,df2,how='inner',on='STATE/UT')


# In[55]:


df5


# In[56]:


df6=pd.merge(df3,df4,how='outer',on='DISTRICT')


# In[57]:


df5.info()


# In[58]:


df7=pd.concat([df1,df2,df3,df4],axis=1)


# In[59]:


df7


# In[60]:


df7.dropna(inplace=True)


# In[61]:


df7


# In[62]:


df7.info()


# In[63]:


# split train test data
y=df7['TOTAL IPC CRIMES']
x=df7.drop(columns=['TOTAL IPC CRIMES','STATE/UT','DISTRICT'])


# In[64]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# In[65]:


# Data scaling.formula Z=(x-mean)/std
scaler = StandardScaler()
x_scaled=scaler.fit_transform(x)


# In[66]:


x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,test_size=0.25,random_state=542)


# import needed libraries. Getting pypodbc to work properly took several hours.
# from base64 import encode
import pandas as pd
# import numpy as np
import pyodbc as odbc
# test line

#read csv into dataframe
df = pd.read_csv("C:\\Users\\natha\\Documents\\NursingHome2020Python\\Nursing_Home_Deficiencies_in_Utah_2020.csv")

#cleaning columns to appropriate format
#DATA CLEAN
#seeing data columns 
# print(df.columns)
# str(df)
# print(df.dtypes)
#The syntax is different for converting an object to a string, I wonder why? TJ helped
df["Federal_Provider_Number"] = df["Federal_Provider_Number"].astype('string')
df["Provider Name"] = df["Provider Name"].astype('string')
df["Provider City"] = df["Provider City"].astype('string')
df["Provider State"] = df["Provider State"].astype('string')
df['Survey Date'] = pd.to_datetime(df['Survey Date'])
df["Deficiency Category"] = df["Deficiency Category"].astype('string')
df["Deficiency Corrected"] = df["Deficiency Corrected"].astype('string')
df["Deficiency Description"] = df["Deficiency Description"].astype('string')

#making variable wtih correct columns
column_names = ['Federal_Provider_Number','Provider Name', 'Provider City',
                 'Provider State','Provider Zip Code', 'Survey Date',
                 'Deficiency Category','Deficiency Description','Deficiency Corrected']
#create new dataframe with correct columns
df_columns = df[column_names]
#print(df_columns)

# #DB info
DRIVER = "SQL Server"
SERVER_NAME="LAPTOP-AKB9MUS2"
DATABASE_NAME = 'NursingHome2020'
#create sql server connection string
#this function was not allowing me to create a connection string, debug later
# def connection_string(driver, server_name, database_name):
#     cnx_string = """
#         DRIVER = {{{driver}}};
#         SERVER = {server_name};
#         DATABASE = {database_name};
#         Trust_Connection=yes;
#     """
#     return cnx_string
# create db connection instance
try:
    conn = odbc.connect('DRIVER=SQL SERVER;SERVER=LAPTOP-AKB9MUS2;DATABASE=NursingHome2020;Trust_Connection=yes')
except odbc.DatabaseError as e :
    print ('Database error:')
    print(str(e.value[1]))
except odbc.Error as e :
    print('Connection Error')
    print(str(e.value[1]))

#make sql statements
sql_insert ="""
    INSERT INTO NursingHomeComplaints 
    (
    Federal_Provider_Number,
    Provider_Name,
    Provider_City,
    Provider_State,
    Provider_ZipCode,
    Survey_Date,
    Deficiency_Category,
    Deficiency_Description,
    Deficiency_Corrected
    )
    VALUES(?,?,?,?,?,?,?,?,?)
"""
#create cursor exception
try:
    cursor = conn.cursor()
    cursor.executemany(sql_insert,df_columns.values.tolist())
    cursor.commit();
except Exception as e:
    cursor.rollback()
    print(str(e[1]))
finally:
    cursor.close()
    conn.close()





import sqlite3
import pandas as pd
import os

ruta = os.getcwd()

path=(f"{ruta}\db_empresa.db")
sqliteConnection = sqlite3.connect(path)
cursor = sqliteConnection.cursor()

#CODIGO PARA MIRAR TODAS LAS TABLAS CREADAS

#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print(cursor.fetchall())

#vista de datos normal
#query = 'SELECT  *FROM DEPARTAMENTO limit 2'
#cursor.execute(query)
#output = cursor.fetchall()
#for row in output
#   print(row)
    
#vista de datos con pandas
query = "SELECT  *FROM DEPARTAMENTO limit 1"
pd.read_sql_query(query, sqliteConnection).head(1)    
    
    


















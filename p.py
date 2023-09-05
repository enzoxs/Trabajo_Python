import sqlite3
import pandas as pd
import os 

ruta = os.getcwd()

path=(f"{ruta}\db_empresassss.db")
sqliteConnection = sqlite3.connect(path)
cursor = sqliteConnection.cursor()


"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import numpy as np
import re
from datetime import datetime

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)

    df = df.drop(['Unnamed: 0'], axis=1)
    for i in df:
      if(i=="fecha_de_beneficio"):
        df[i] = df[i].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))
        continue
      elif(i=="monto_del_credito"):
        df[i] = df[i].str.replace('$ ', '', regex=False)
        df[i] = df[i].str.replace(',', '', regex=False)
        df[i] = df[i].str.replace('.00', '', regex=False)
        df[i] = df[i].astype(int)
        continue
        
      elif(df[i].dtype!="int64" and df[i].dtype!="float64"):
        df[i] = df[i].str.lower()
        df[i] = df[i].str.replace('-', ' ', regex=False)
        df[i] = df[i].str.replace('_', ' ', regex=False)
        
    df.drop_duplicates(inplace=True)
    return df

clean_data()

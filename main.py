from lectura_de_datos.Api.estraccion_de_datos_por_api import get_df , obtener_namecolumns, Separacion, guardar_dataframes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
id = "055A4D"
inicio = "2025-01-01"
fin = "2025-01-01"
url = "https://www.simem.co/backend-files/api/detalle-datos-publicos?datasetId={dataset_id}"

print("Etapa1")
#get_df(id,inicio,fin)
print("Etapa2")
colums = obtener_namecolumns(id, url)
print(colums)
print("Etapa3")
df = pd.read_csv("archivo.csv")
print('Etapa4')
df_xy_principal , df_atributos = Separacion(colums,df)
guardar_dataframes(df_xy_principal = df_xy_principal,
                   df_atributos = df_atributos)
print(df_xy_principal.head())
print(df_atributos.head())




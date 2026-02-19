from lectura_de_datos.Api.estraccion_de_datos_por_api import get_df , obtener_namecolumns, Separacion
import pandas as pd

id = "055A4D"
inicio = "2025-01-01"
fin = "2025-02-01"
url = "https://www.simem.co/backend-files/api/detalle-datos-publicos?datasetId={dataset_id}"

print("Etapa1")
#get_df(id,inicio,fin)
print("Etapa2")
colums = obtener_namecolumns(id, url)
print(colums)
print("Etapa3")
df = pd.read_csv("archivo.csv")
print('Etapa4')
df1 , df2 = Separacion(colums,df)
print(df1.head())
print(df2.head())
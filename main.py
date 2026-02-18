from lectura_de_datos.Api.estraccion_de_datos_por_api import get_df
from lectura_de_datos.Api.identificacion_de_columnas import obtener_namecolumns

id = "055A4D"
inicio = "2025-01-01"
fin = "2025-05-01"
url = "https://www.simem.co/backend-files/api/detalle-datos-publicos?datasetId={dataset_id}"

print("Etapa1")
get_df(id,inicio,fin)
print("Etapa2")
colums = obtener_namecolumns(id, url)
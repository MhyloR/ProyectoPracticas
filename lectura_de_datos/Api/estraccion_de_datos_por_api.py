import sys
import os
from pydataxm.pydatasimem import ReadSIMEM, CatalogSIMEM
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates

catalogo = CatalogSIMEM(catalog_type='Datasets')
df_catalogo = catalogo.get_data()

dataset_id = '95443E'
fecha_inicio = '2024-09-28'
fecha_fin = '2026-10-28'
simem = ReadSIMEM(dataset_id, fecha_inicio, fecha_fin)

df_genreal = simem.main()
df_genreal.to_csv("archivo.csv", index=False, sep=";")
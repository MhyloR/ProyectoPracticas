import sys
import os
from pydataxm.pydatasimem import ReadSIMEM, CatalogSIMEM
import pandas as pd


def get_df(id, fecha_inicio, fecha_final):
    catalogo = CatalogSIMEM(catalog_type='Datasets')
    df_catalogo = catalogo.get_data()

    dataset_id = id
    fecha_inicio = fecha_inicio
    fecha_fin = fecha_final
    simem = ReadSIMEM(dataset_id, fecha_inicio, fecha_fin)

    df_genreal = simem.main()
    df_genreal.to_csv("archivo.csv")

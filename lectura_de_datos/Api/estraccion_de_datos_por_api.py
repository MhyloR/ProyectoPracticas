import sys
import os
from pydataxm.pydatasimem import ReadSIMEM, CatalogSIMEM
import pandas as pd

def get_df(id, fecha_inicio, fecha_final):
    catalogo = CatalogSIMEM(catalog_type='Datasets')
    df_catalogo = catalogo.get_data()

    dataset_id = id
    fecha_fin = fecha_final
    simem = ReadSIMEM(dataset_id, fecha_inicio, fecha_fin)
    df_general = simem.main()

    # ---------- Crear carpeta "salidas" un nivel arriba ----------
    base_dir = os.path.dirname(os.path.abspath(__file__))
    carpeta_superior = os.path.abspath(os.path.join(base_dir, "../.."))
    carpeta_salidas = os.path.join(carpeta_superior, "salidas")
    os.makedirs(carpeta_salidas, exist_ok=True)

    # Construir nombre de archivo (puedes personalizarlo)
    nombre_csv = "archivo.csv"  # o f"{dataset_id}_{fecha_inicio}_{fecha_fin}.csv"
    ruta_csv = os.path.join(carpeta_salidas, nombre_csv)

    # Guardar CSV (evita índice como columna)
    if df_general is None:
        # Si por algún motivo la librería retorna None, guardamos un CSV vacío
        df_general = pd.DataFrame()
        print("Advertencia: ReadSIMEM.main() devolvió None. Se guarda DataFrame vacío.")

    df_general.to_csv(ruta_csv, index=False)
    print(f"CSV guardado en: {ruta_csv}")

    return df_general


import sys
import os
from pydataxm.pydatasimem import ReadSIMEM, CatalogSIMEM
import pandas as pd

def get_df(id, fecha_inicio, fecha_final, nombre_csv="archivo.csv"):
    # --- Obtención de datos ---
    catalogo = CatalogSIMEM(catalog_type='Datasets')
    df_catalogo = catalogo.get_data()

    dataset_id = id
    fecha_fin = fecha_final
    simem = ReadSIMEM(dataset_id, fecha_inicio, fecha_fin)
    df_general = simem.main()

    # --- Calcular ruta DOS niveles arriba, sin crear carpetas ---
    # Si __file__ no existe (Jupyter/REPL), usamos el cwd
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        base_dir = os.getcwd()  # entorno interactivo

    carpeta_dos_arriba = os.path.abspath(os.path.join(base_dir, "..", ".."))

    # Verificación: no crear carpetas; si no existe, fallar con mensaje claro
    if not os.path.isdir(carpeta_dos_arriba):
        raise FileNotFoundError(
            f"La carpeta dos niveles arriba no existe o no es accesible: {carpeta_dos_arriba}"
        )

    ruta_csv = os.path.join(carpeta_dos_arriba, nombre_csv)

    # Manejo defensivo si la librería devuelve None
    if df_general is None:
        df_general = pd.DataFrame()
        print("Advertencia: ReadSIMEM.main() devolvió None. Se guarda DataFrame vacío.")

    # Guardar CSV (no se crean carpetas)
    df_general.to_csv(ruta_csv, index=False)
    print(f"CSV guardado en: {ruta_csv}")

    return df_general
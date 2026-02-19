import sys
import os
from pydataxm.pydatasimem import ReadSIMEM, CatalogSIMEM
import pandas as pd
import requests
from typing import List, Any, Dict, Union

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


def obtener_namecolumns(dataset_id: str, url_template: str, timeout: int = 200) -> List[str]:
    
    # 1) Construir la URL reemplazando el placeholder exactamente como lo tienes en tu código
    if "{dataset_id}" not in url_template:
        raise ValueError("El url_template debe contener el placeholder {dataset_id}")
    url = url_template.format(dataset_id=dataset_id)

    # 2) Llamar al endpoint
    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()

    # 3) Parsear JSON
    try:
        data = resp.json()
    except ValueError as e:
        raise ValueError(f"La respuesta no es JSON válido. Error: {e}")

    if data is None:
        raise ValueError("La respuesta JSON está vacía (None).")

    # 4) Buscar recursivamente 'Columns' y extraer 'nameColumn'
    def _find_namecolumns(obj: Union[Dict[str, Any], List[Any]]) -> List[str]:
        found: List[str] = []
        columns_keys_lower = {"columns"}  # case-insensitive ('Columns' o 'columns')

        def _walk(node: Any):
            if isinstance(node, dict):
                for k, v in node.items():
                    # ¿Esta clave es 'Columns' (sin importar mayúsculas)?
                    if str(k).lower() in columns_keys_lower:
                        # v puede ser list o dict. Extraer 'nameColumn' en formatos comunes.
                        if isinstance(v, list):
                            for item in v:
                                if isinstance(item, dict) and "nameColumn" in item:
                                    found.append(item["nameColumn"])
                        elif isinstance(v, dict):
                            # Buscar en subclaves típicas
                            candidates_list = None
                            for ck in ("items", "data", "list", "values"):
                                if ck in v and isinstance(v[ck], list):
                                    candidates_list = v[ck]
                                    break
                            if candidates_list:
                                for item in candidates_list:
                                    if isinstance(item, dict) and "nameColumn" in item:
                                        found.append(item["nameColumn"])
                            else:
                                # Último recurso: barrer el dict y listas internas
                                for subv in v.values():
                                    if isinstance(subv, dict) and "nameColumn" in subv:
                                        found.append(subv["nameColumn"])
                                    elif isinstance(subv, list):
                                        for item in subv:
                                            if isinstance(item, dict) and "nameColumn" in item:
                                                found.append(item["nameColumn"])
                    # Seguir recorriendo el árbol
                    _walk(v)
            elif isinstance(node, list):
                for it in node:
                    _walk(it)

        _walk(obj)

        # Devolver únicos conservando el orden
        seen = set()
        unique = []
        for x in found:
            if x not in seen:
                unique.append(x)
                seen.add(x)
        return unique

    return _find_namecolumns(data)


def Separacion(columnas, archivo):
        
    while True:
        var_x = input("Variable eje X: ").strip()
        if var_x in columnas:
            break

    while True:
        var_y = input("Variable eje y: ").strip()
        if var_y in columnas:
            break

    df_general = archivo[[var_x, var_y]].copy()
    

    try:
        # Tu formato “ideal”
        df_general[var_x] = pd.to_datetime(df_general[var_x], format='%Y-%m-%d %H:%M:%S')
    except Exception:
        # Fallback flexible si hay variaciones
        df_general[var_x] = pd.to_datetime(df_general[var_x], errors='coerce', dayfirst=False)

    df_atributos = archivo.drop([var_x, var_y], axis=1)

    return df_general, df_atributos
        

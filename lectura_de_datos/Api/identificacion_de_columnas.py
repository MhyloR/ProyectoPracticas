import requests
from typing import List, Any, Dict, Union

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


##EJEMPLO DE USO###
#dataset_id = "75f675"
#url_template = "https://www.simem.co/backend-files/api/detalle-datos-publicos?datasetId={dataset_id}"


#columnas = obtener_namecolumns(dataset_id, url_template)
#print("nameColumn encontrados:", columnas)
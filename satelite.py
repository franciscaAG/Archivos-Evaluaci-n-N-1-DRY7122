import requests
import time
from datetime import datetime

def obtener_posicion_iss():
    """
    Recupera la localización actual de la Estación Espacial Internacional.
    Devuelve latitud, longitud y marca de tiempo.
    """
    url = "http://api.open-notify.org/iss-now.json"
    try:
        r = requests.get(url)
        r.raise_for_status()
        info = r.json()

        if "iss_position" in info:
            lat = float(info["iss_position"]["latitude"])
            lon = float(info["iss_position"]["longitude"])
            tiempo = info["timestamp"]
            return lat, lon, tiempo
        else:
            print("Respuesta de API no contiene datos esperados.")
            return None, None, None

    except Exception as err:
        print(f"Fallo en la conexión: {err}")
        return None, None, None

def calcular_grados_por_hora(valor_inicial, valor_final, segundos):
    """
    Estima la velocidad angular en grados por hora.
    """
    cambio = valor_final - valor_inicial
    return (cambio / segundos) * 3600

# --- Inicio del monitoreo ---
print("Seguimiento activo de la ISS...")

# Obtener posición inicial
lat_anterior, lon_anterior, t_anterior = obtener_posicion_iss()

# Ejecutar indefinidamente
while True:
    time.sleep(60)  # Esperar 60 segundos

    lat_nueva, lon_nueva, t_nueva = obtener_posicion_iss()

    # Verifica si la consulta fue exitosa
    if None not in (lat_nueva, lon_nueva, lat_anterior, lon_anterior):
        delta_t = t_nueva - t_anterior

        velocidad_lat = calcular_grados_por_hora(lat_anterior, lat_nueva, delta_t)
        velocidad_lon = calcular_grados_por_hora(lon_anterior, lon_nueva, delta_t)

        ahora = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n[{ahora} UTC]")
        print(f"Latitud actual:  {lat_nueva:.6f}°")
        print(f"Longitud actual: {lon_nueva:.6f}°")
        print(f"Velocidad estimada:")
        print(f"   Latitud : {velocidad_lat:.6f}°/h")
        print(f"   Longitud: {velocidad_lon:.6f}°/h")

        # Actualizar coordenadas y tiempo
        lat_anterior, lon_anterior, t_anterior = lat_nueva, lon_nueva, t_nueva
    else:
        print("No se pudo obtener la información. Reintentando...")
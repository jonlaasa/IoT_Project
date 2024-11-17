import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS, Point

# Parámetros de conexión
url = "http://localhost:8086"  # URL de tu servidor InfluxDB
token = "hpAByb0Y-avojmlGuAkEt4zNpuziVdlTqVsE9AcjhAjP_Yg1BTz73jaZkI6U-wedXcqE6UgdjqfhDutQEsyZ5Q=="  # Token de autenticación
org = "iot"  # Nombre de la organización
bucket = "measurements"  # Nombre del bucket donde guardarás los datos

# Crear el cliente de InfluxDB
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

# Definir la función para escribir en InfluxDB
def write_to_influxdb(id, heart_rate, oxygen_in_blood, body_temperature, ambient_temperature, timestamp):
  
    # Crear un punto de datos con los valores recibidos
    point = Point("measurement") \
        .tag("id", str(id)) \
        .field("heart_rate", heart_rate) \
        .field("oxygen_in_blood", oxygen_in_blood) \
        .field("body_temperature", body_temperature) \
        .field("ambient_temperature", ambient_temperature) \
        .field("time", timestamp)

    # Escribir el punto en InfluxDB
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket=bucket, org=org, record=point)
    print("Datos escritos en InfluxDB para paciente {id}.")

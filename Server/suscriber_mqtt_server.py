import paho.mqtt.client as mqtt
## UTILIZAMOS OTRO SCRIPT PARA HACER LA INGESTA DE DATOS
from load_influx import write_to_influxdb
# Añadir funcion de carga de bd 
import sqlite3

# Definir la función de callback para manejar los mensajes recibidos
def on_message(client, userdata, message):
    print(f"Mensaje recibido en {message.topic}: {message.payload.decode()}")

    # Dividir el mensaje recibido por comas
    data = message.payload.decode().split(", ")
    
    # Asignar cada valor a una variable, ajustando para que el ID sea el segundo elemento
    measurement_type = data[0]  # "medicion"
    print(f"Measurement Type: {measurement_type}")
    patient_id = data[1]  # ID del paciente
    print(f"ID: {patient_id}")
    heart_rate = float(data[2])  # Frecuencia cardíaca
    print(f"Heart Rate: {heart_rate} bpm")
    spo2 = float(data[3])  # Saturación de oxígeno
    print(f"SpO2: {spo2}%")
    temperature_patient = float(data[4])  # Temperatura del paciente
    print(f"Patient Temperature: {temperature_patient} °C")
    ambient_temperature = float(data[5])  # Temperatura ambiente
    print(f"Ambient Temperature: {ambient_temperature} °C")
    timestamp = data[6]  # Timestamp

    # Imprimir cada variable
    print(f"Measurement Type: {measurement_type}")
    print(f"ID: {patient_id}")
    print(f"Heart Rate: {heart_rate} bpm")
    print(f"SpO2: {spo2}%")
    print(f"Patient Temperature: {temperature_patient} °C")
    print(f"Ambient Temperature: {ambient_temperature} °C")
    print(f"Timestamp: {timestamp}")

    # Llamar a la función para escribir en InfluxDB
    write_to_influxdb(
        id=patient_id,
        heart_rate=heart_rate,
        oxygen_in_blood=spo2,
        body_temperature=temperature_patient,
        ambient_temperature=ambient_temperature,
        timestamp=timestamp
    )

# Configuración del cliente MQTT para suscripción
client = mqtt.Client()

# Asignar la función de callback para recibir mensajes
client.on_message = on_message

# Conexión al broker
client.connect("test.mosquitto.org", 1883)

# Suscribirse al tópico
client.subscribe("watch/mediciones")


# def listar_tablas():
#     """Conecta a la base de datos 'db.sqlite3' y lista los nombres de las tablas."""
#     try:
#         # Conectar a la base de datos (nombre actualizado)
#         conexion = sqlite3.connect("db.sqlite3")  # Asegúrate de que el archivo tenga este nombre
#         cursor = conexion.cursor()
        
#         # Consultar los nombres de las tablas
#         cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#         tablas = cursor.fetchall()
        
#         # Mostrar las tablas
#         if tablas:
#             print("Tablas disponibles:")
#             for tabla in tablas:
#                 print(tabla[0])
#         else:
#             print("No se encontraron tablas en la base de datos.")
            
#     except sqlite3.Error as e:
#         print(f"Error al acceder a la base de datos: {e}")
#     finally:
#         # Cerrar la conexión
#         if conexion:
#             conexion.close()

# # Llamar a la función
# listar_tablas()

import sqlite3

def construir_diccionarios():
    """Crea dos diccionarios a partir de las tablas especificadas."""
    try:
        # Conectar a la base de datos
        conexion = sqlite3.connect("db.sqlite3")
        cursor = conexion.cursor()
        
        # Diccionario 1: Mapeo de pacientes a familiares
        dict_paciente_familiares = {}
        cursor.execute("SELECT * FROM appIoTproject_pacientefamiliarunion")
        filas_union = cursor.fetchall()
        for fila in filas_union:
            paciente_id = fila[1]  # Segundo valor de la fila
            familiar_id = fila[2]  # Tercer valor de la fila
            if paciente_id not in dict_paciente_familiares:
                dict_paciente_familiares[paciente_id] = []
            dict_paciente_familiares[paciente_id].append(familiar_id)
        
        # Diccionario 2: Mapeo de pacientes a sus valores
        dict_paciente_datos = {}
        cursor.execute("SELECT * FROM appIoTproject_paciente")
        filas_paciente = cursor.fetchall()
        for fila in filas_paciente:
            paciente_id = fila[0]  # Primer valor de la fila
            valores = fila[1:]    # Todos los demás valores
            dict_paciente_datos[paciente_id] = list(valores)
        
        return dict_paciente_familiares, dict_paciente_datos
    
    except sqlite3.Error as e:
        print(f"Error al acceder a las tablas: {e}")
        return {}, {}
    finally:
        # Cerrar la conexión
        if conexion:
            conexion.close()

# Construir y mostrar los diccionarios
dict_familiares, dict_datos = construir_diccionarios()

print("Diccionario de pacientes y sus familiares:")
print(dict_familiares)

print("\nDiccionario de pacientes y sus datos:")
print(dict_datos) 

#### SIMULACION TELEGRAM #########
from twilio.rest import Client

# Tus credenciales de Twilio
account_sid = 'ACe985ad25436af167b58108688517d76e'  # SID de tu cuenta
auth_token = 'd2bce0037b1ae2976fda8efc66d630d2'  # Token de autenticación

# Crear el cliente Twilio
client = Client(account_sid, auth_token)

# Enviar el mensaje de WhatsApp
message = client.messages.create(
    body='¡Hola! Este es un mensaje de prueba enviado automáticamente desde Twilio.',
    from_='whatsapp:+14155238886',  # Número de WhatsApp proporcionado por Twilio
    to='whatsapp:+34688850837'  # Reemplaza con tu número de WhatsApp (con el prefijo 'whatsapp:')
)

# Imprimir el SID del mensaje enviado
print(f'Mensaje enviado con SID: {message.sid}')



#RECOVERY:  9EZMLAAWRKQNWNGQ776UAVRS


# Mantener el cliente activo para recibir mensajes
client.loop_forever()

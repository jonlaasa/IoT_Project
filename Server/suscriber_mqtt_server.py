import paho.mqtt.client as mqtt
## UTILIZAMOS OTRO SCRIPT PARA HACER LA INGESTA DE DATOS
from load_influx import write_to_influxdb

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

# Mantener el cliente activo para recibir mensajes
client.loop_forever()

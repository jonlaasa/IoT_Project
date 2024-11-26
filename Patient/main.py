import time
import os
from datetime import datetime
import heartO2Patient  # Módulo para el sensor de ritmo cardíaco y SpO2
import temperaturePatient  # Módulo para el sensor de temperatura del paciente
import temperatureAmbient  # Módulo para obtener la temperatura ambiental
import paho.mqtt.client as mqtt  # Importar la librería MQTT

# Configuración del cliente MQTT para publicación
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)

# Crear la carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

# Función para registrar los datos en los archivos de log con el timestamp
def log_data(file_name, data, timestamp):
    """Registra los datos con el timestamp actual en el archivo de log."""
    with open(file_name, "a") as file:
        file.write(f"{timestamp}: {data}\n")

if __name__ == "__main__":
    while True:
        # Calcular el timestamp solo una vez
        current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        # Obtener los valores de los sensores
        hb, spo2 = heartO2Patient.get_heart_rate_and_spo2()  # De `heartO2Patient.py`
        temperature_patient = temperaturePatient.get_temperature()  # De `temperaturePatient.py`
        ambient_temperature = temperatureAmbient.get_ambient_temperature()  # De `temperatureAmbient.py`

        # Mostrar los resultados en la terminal
        print(f"Heart Rate: {hb} bpm, SpO2: {spo2}%")
        print(f"Temperature (Patient): {temperature_patient:.1f} °C")
        if ambient_temperature is not None:
            print(f"Ambient Temperature: {ambient_temperature} °C")

        # Registrar los datos en los archivos de log con el mismo timestamp
        log_data("logs/heart_rate_log.txt", f"Pulse: {hb}, SpO2: {spo2}%", current_time)
        log_data("logs/temperature_patient_log.txt", f"Temperature (Patient): {temperature_patient:.1f} °C", current_time)
        if ambient_temperature is not None:
            log_data("logs/ambient_temperature_log.txt", f"Ambient Temperature: {ambient_temperature} °C", current_time)

        # Enviar los datos al tópico MQTT en el formato especificado
        message = f"Medicion, 1, {hb}, {spo2}, {temperature_patient:.1f}, {ambient_temperature}, {current_time}"
        client.publish("watch/mediciones", message)

        # Pausa de 2 segundos antes de la siguiente lectura
        time.sleep(10)

    # Desconectar al final (esto realmente solo se ejecutará si sales del bucle, por ejemplo, con un KeyboardInterrupt)
    client.disconnect()


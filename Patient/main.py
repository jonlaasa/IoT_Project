import time
import os
from datetime import datetime
import heartO2Patient  # Módulo para el sensor de ritmo cardíaco y SpO2
import temperaturePatient  # Módulo para el sensor de temperatura del paciente
import temperatureAmbient  # Módulo para obtener la temperatura ambiental

# Crear la carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

# Función para registrar los datos en los archivos de log con el timestamp
def log_data(file_name, data):
    """Registra los datos con la fecha y hora actuales en el archivo de log."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, "a") as file:
        file.write(f"{current_time}: {data}\n")

if __name__ == "__main__":
    while True:
        # Obtener los valores de los sensores
        hb, spo2 = heartO2Patient.get_heart_rate_and_spo2()  # De `heartO2Patient.py`
        temperature_patient = temperaturePatient.get_temperature()  # De `temperaturePatient.py`
        ambient_temperature = temperatureAmbient.get_ambient_temperature()  # De `temperatureAmbient.py`

        # Mostrar los resultados en la terminal
        print(f"Heart Rate: {hb} bpm, SpO2: {spo2}%")
        print(f"Temperature (Patient): {temperature_patient:.1f} °C")
        if ambient_temperature is not None:
            print(f"Ambient Temperature: {ambient_temperature} °C")

        # Registrar los datos en los archivos de log
        log_data("logs/heart_rate_log.txt", f"Pulse: {hb}, SpO2: {spo2}%")
        log_data("logs/temperature_patient_log.txt", f"Temperature (Patient): {temperature_patient:.1f} °C")
        if ambient_temperature is not None:
            log_data("logs/ambient_temperature_log.txt", f"Ambient Temperature: {ambient_temperature} °C")
        
        # Pausa de 2 segundos antes de la siguiente lectura
        time.sleep(2)


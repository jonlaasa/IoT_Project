# heart_rate_o2.py
import max30100

# Crear objeto del sensor
mx30 = max30100.MAX30100()
mx30.enable_spo2()

def get_heart_rate_and_spo2():
    """Obtiene una lectura de heart rate y SpO2."""
    mx30.read_sensor()

    # Obtener las lecturas de heart rate y SpO2
    hb = int(mx30.ir / 100)  # Heart rate (latidos por minuto)
    spo2 = int(mx30.red / 100)  # SpO2 (nivel de oxígeno en sangre)

    return hb, spo2

import RPi.GPIO as GPIO
import time

def control_led():
    """
    Controla un LED conectado al pin GPIO 24, encendiéndolo por 3 segundos.
    """
    LED_PIN = 24  # Pin GPIO donde está conectado el LED

    # Configuración inicial
    GPIO.setmode(GPIO.BCM)  # Usar numeración BCM
    GPIO.setup(LED_PIN, GPIO.OUT)  # Configurar el pin como salida

    try:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Encender LED
        print("LED encendido")
        time.sleep(3)  # Esperar 3 segundos
        GPIO.output(LED_PIN, GPIO.LOW)  # Apagar LED
        print("LED apagado")
    except KeyboardInterrupt:
        print("Interrupción por teclado detectada.")
    finally:
        GPIO.cleanup()  # Liberar recursos GPIO


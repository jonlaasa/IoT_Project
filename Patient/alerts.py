import paho.mqtt.client as mqtt
from led import control_led

# Función de callback que se ejecuta cuando se recibe un mensaje
def on_message(client, userdata, message):
    print(f"Mensaje recibido en el tópico '{message.topic}': {message.payload.decode()}")
    control_led()

# Configuración del cliente MQTT
def main():
    client = mqtt.Client()

    # Configurar la función callback para manejar mensajes
    client.on_message = on_message

    # Conectarse al servidor MQTT
    client.connect("test.mosquitto.org", 1883)

    # Suscribirse al tópico watch/alerts
    client.subscribe("alerts")
    print("Esperando mensajes en el tópico 'alerts'...")

    # Iniciar un loop infinito para esperar mensajes
    client.loop_forever()

if __name__ == "__main__":
    main()


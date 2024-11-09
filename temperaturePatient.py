import board
from adafruit_bme280 import basic as adafruit_bme280

# Configuración del I2C
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

def get_temperature():
    """Obtiene la temperatura del sensor BME280."""
    temperature = bme280.temperature
    return temperature

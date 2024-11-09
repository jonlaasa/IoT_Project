import requests

def get_ambient_temperature():
    """Obtiene la temperatura ambiental desde la API de Open-Meteo."""
    # Define la URL y parámetros con la latitud y longitud exactas de la Universidad de Deusto
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 43.272222222222,  # Latitud de la Universidad de Deusto
        "longitude": -2.9458333333333, # Longitud de la Universidad de Deusto
        "current_weather": "true"
    }

    # Realiza la solicitud GET con los parámetros
    response = requests.get(url, params=params)

    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        # Analiza la respuesta JSON
        weather_data = response.json()
        ambient_temperature = weather_data["current_weather"]["temperature"]
        return ambient_temperature
    else:
        print("Error:", response.status_code)
        return None


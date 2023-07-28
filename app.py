import requests
import json
import tweepy

#Datos del API Clima
q = 'Buenos Aires'
lang = 'es'
key = 'fb74469b209446fdb0b220519232707'
url = f'https://api.weatherapi.com/v1/current.json?key={key}&q={q}&lang={lang}'

#Datos para redacción del texto
text = str()

#Datos para API Twitter
CONSUMER_KEY = "GrVXfFaTBEm9TO8WVEru7lvRw"
CONSUMER_KEY_SECRET = "MQ4pLlL6q0wbwQ64WBPrTLykCD8NzI1fXy1o7BySciF0uNgEsZ"
ACCESS_TOKEN = "1539417355276759040-QWP3YygUoNP3wi58H54aB83u1R3SFv"
ACCESS_TOKEN_SECRET = "iYuas2NZauZz6Leyblff9zQJP97oV9mxR5l1kZcGb3OrS"
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAALo8pAEAAAAA7VgI2kgY9ayJyZVbQ3cs2kP7lHw%3DstWCkQI0ObmNatIfVcDkUbgzkA09e9YedVjv0DSnOJmt29NCRI"
api = tweepy.Client(bearer_token=BEARER_TOKEN,
                    access_token=ACCESS_TOKEN,
                    access_token_secret=ACCESS_TOKEN_SECRET,
                    consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_KEY_SECRET)

#obtener clima
def get_climate():
    r = requests.get(url)
    return json.loads(r.content)

# redactar texto y limpiar datos
def get_text(data:dict):
    current = data.get('current')
    location = data.get('location')
    
    region = f"{location.get('name')}, {location.get('region')}"
    last_updated = current.get('last_updated')
    temp_c = current.get('temp_c')
    feelslike_c =current.get('feelslike_c')
    wind_vel = current.get('wind_kph')
    wind_dir_degree = current.get('wind_degree')
    pressure_mb = current.get('pressure_mb')
    precip_mm = current.get('precip_mm')
    humidity = current.get('humidity')
    cloud = current.get('cloud')
    vis_km = current.get('vis_km')
    weather_condition_text = current.get('condition').get('text') 

    text = f"""
    {region} 📍
Última actualización: {last_updated} ⏱️
🌡️ Temp: {temp_c}°C, Sensación térmica: {feelslike_c}°C
☁️ Condición: {weather_condition_text}
💨 Viento: {wind_vel} km/h, Dirección: {wind_dir_degree}°
📊 Presión: {pressure_mb} mb, Precipitación: {precip_mm} mm
💧 Humedad: {humidity}% , Nubes: {cloud}% , Visibilidad: {vis_km} km
#clima #tiempo"
    """
    return text

def create_tweet(post):
    api.create_tweet(text=post)

if __name__ == '__main__':
    data = get_climate()
    post = get_text(data)
    create_tweet(post)
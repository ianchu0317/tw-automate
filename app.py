import requests
import pprint
import json

#Datos del API
q = 'Buenos Aires'
lang = 'es'
key = 'fb74469b209446fdb0b220519232707'
url = f'https://api.weatherapi.com/v1/current.json?key={key}&q={q}&lang={lang}'

#Datos para redacción del texto
text = str()
weather_condition_icon = str()

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
    weather_condition_text = current.get('condition').get('text') 
    weather_condition_icon = current.get('condition').get('icon')
    wind_vel = current.get('wind_kph')
    wind_dir_degree = current.get('wind_degree')
    pressure_mb = current.get('pressure_mb')
    precip_mm = current.get('precip_mm')
    humidity = current.get('humidity')
    cloud = current.get('cloud')
    vis_km = current.get('vis_km')

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

if __name__ == '__main__':
    data = get_climate()
    text = get_text(data)
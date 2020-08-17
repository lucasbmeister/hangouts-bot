import requests
from app_util import sendMessage, getConfig, formatNumber
from datetime import datetime, timezone, timedelta


def handleWeatherCommand(browser, chatBoxInput, days=0):
    key = getConfig('WEATHER', 'api_key')
    days=int(days)
    params = {
        'key': key,
        'q': 'Joinville'
    }

    if days > 0:
        params['days'] = days

    r = requests.get(
        'https://api.weatherapi.com/v1/forecast.json', params=params)
    resp = r.json()

    if days > 0:
        forecast = resp['forecast']['forecastday'][days - 1]
        date = datetime.strptime(forecast['date'], '%Y-%m-%d')
        weather = {
            'temp_c': formatNumber(forecast["day"]["maxtemp_c"]),
            'rain': formatNumber(float(forecast["day"]["daily_chance_of_rain"])),
            'humidity': formatNumber(forecast["day"]["avghumidity"]),

        }
    else:
        forecast = resp["current"]
        date = datetime.strptime(forecast['last_updated'], '%Y-%m-%d %H:%M')
        weather = {
            'temp_c': formatNumber(forecast["temp_c"]),
            'sensation': formatNumber(forecast["feelslike_c"]),
            'humidity': formatNumber(forecast["humidity"]),
        }
        
    message = f' (BOT) Clima para o dia {date.strftime("%d/%m/%Y")}:\n'
    message += f' Temperatura: {weather["temp_c"]}°C\n' 
    message += f' Humidade: {weather["humidity"]}%\n'
    if days > 0:
        message += f' Chance Chuva: {weather["rain"]}%\n'
    else:
        message += f' Sensação : {weather["sensation"]}°C'


    sendMessage(browser, chatBoxInput, message)


weather_command = {
    'command': '!previsao',
    'function': handleWeatherCommand,
    'args': [],
    'acceptParams': True,
    'description': 'Retorna o clima atual ou os próximos dias conforme parâmetro. Ex.: !previsao [2] //retorna previsão para daqui dois dias'
}

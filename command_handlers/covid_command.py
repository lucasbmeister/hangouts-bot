import requests
from app_util import sendMessage, formatNumber


def handleCovidCommand(browser, chatBoxInput, country='BR'):

    r = requests.get(f'http://corona-api.com/countries/{country}')
    resp = r.json()

    if 'message' in resp:
        sendMessage(browser, chatBoxInput,
                    f'(BOT) País inválido (utilizar código ISO 3166-1 alpha-2 [BR, US, ...])')
    else:
        data = resp['data']
        message = f'(BOT) Informações {data["name"]}:\n'
        message += f' - Hoje:\n'
        message += f' * Mortes: {formatNumber(data["today"]["deaths"])}\n'
        message += f' * Confirmados: {formatNumber(data["today"]["confirmed"])}\n'
        message += f' - Total Geral:\n'
        message += f' * Mortes: {formatNumber(data["latest_data"]["deaths"])}\n'
        message += f' * Confirmados: {formatNumber(data["latest_data"]["confirmed"])}\n'
        message += f' * Recuperados: {formatNumber(data["latest_data"]["recovered"])}\n'
        message += f' * Críticos: {formatNumber(data["latest_data"]["critical"])}\n\n'
        message += f' Indice Mort.: {formatNumber(data["latest_data"]["calculated"]["death_rate"])}\n\n'

        sendMessage(browser, chatBoxInput, message)


covid_command = {
    'command': '!covid',
    'function': handleCovidCommand,
    'args': [],
    'acceptParams': True,
    'description': 'Mostrar status COVID atual para o Brasil ou, país em parâmetro. Ex. !covid [US]'
}

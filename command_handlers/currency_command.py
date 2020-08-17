import requests
from app_util import sendMessage, formatNumber


def getCurrencyValue(currency1, currency2):
    r = requests.get(
        f'https://economia.awesomeapi.com.br/all/{currency1}-{currency2}')
    json = r.json()
    return json[currency1]['high']


def handleCurrencyCommand(browser, chatBoxInput, currency1='', currency2='BRL'):

    if currency1 == '':
        sendMessage(browser, chatBoxInput,
                    f'(BOT) Moeda não encontrada')
        return

    currency1 = currency1.upper()

    currencies = {
        'USD': 'Dólar Comercial',
        'USDT': 'Dólar Turismo',
        'CAD': 'Dólar Canadense',
        'AUD': 'Dólar Australiano',
        'EUR': 'Euro',
        'GBP': 'Libra Esterlina',
        'ARS': 'Peso Argentino',
        'JPY': 'Iene Japonês',
        'CHF': 'Franco Suíço',
        'CNY': 'Yuan Chinês',
        'YLS': 'Novo Shekel Israelense',
        'BTC': 'Bitcoin',
        'LTC': 'Litecoin',
        'ETH': 'Ethereum',
        'XRP': 'Ripple',
        'BRL': 'Real'
    }

    if currencies.get(currency1) == None:
        sendMessage(browser, chatBoxInput,
                    f'(BOT) Moeda não encontrada')
        return

    value = getCurrencyValue(currency1, currency2)
    sendMessage(browser, chatBoxInput,
                f'(BOT) O valor do(a) {currencies[currency1]} é R$ {formatNumber(float(value))}')


dollar_command = {
    'command': '!dolar',
    'function': handleCurrencyCommand,
    'args': ["USD", "BRL"],
    'description': 'Retorna cotação do dia do dólar'
}

euro_command = {
    'command': '!euro',
    'function': handleCurrencyCommand,
    'args': ["EUR", "BRL"],
    'description': 'Retorna cotação do dia do euro'
}

libra_command = {
    'command': '!libra',
    'function': handleCurrencyCommand,
    'args': ["GBP", "BRL"],
    'description': 'Retorna cotação do dia da libra esterlina'
}

bitcoin_command = {
    'command': '!bitcoin',
    'function': handleCurrencyCommand,
    'args': ["BTC", "BRL"],
    'description': 'Retorna cotação do dia do bitcoin'
}

currency_command = {
    'command': '!moeda',
    'function': handleCurrencyCommand,
    'args': [],
    'acceptParams': True,
    'description': 'Retorna cotação da moeda em parâmetro em reais. Ex.: !moeda [USDT]'
}

import requests
from app_util import sendMessage, formatNumber


def getKeyDescription(key):
    descriptions = {
        "change": "Variação",
        "closingPrice": "Valor Fechamento",
        "eps": "Lucro por Ação",
        "high": "Alta",
        "lastPrice": "Últ. Preço",
        "lastYearHigh": "Alt 52 sem",
        "lastYearLow": "Bai 52 sem",
        "low": "Baixa",
        "marketCap": "Cap. Merc.",
        "name": "Nome",
        "pe": "Índice P/L",
        "priceOpen": "Abertura",
        "shares": "Ações",
        "symbol": "Simbolo",
        "volume": "Volume",
        "volumeAvg": "Média Volume",
        "sector": "Setor",
        "subSector": "Sub-Setor",
        "segment": "Segmento"
    }
    return descriptions[key]


def stockToString(stockInfo):
    stockString = ''
    for key in stockInfo:
        if isinstance(stockInfo[key], (float, int)):
            stockInfo[key] = formatNumber(stockInfo[key])
        stockString += f' {getKeyDescription(key)}: {stockInfo[key]}\n'
    return stockString


def getStockInfo(stock):
    r = requests.get(f'https://mfinance.com.br/api/v1/stocks/{stock}')
    data = r.json()
    return data


def handleStockCommand(browser, chatBoxInput, stock='', info=''):
    message = ''
    if stock != '':
        stockInfo = getStockInfo(stock)
        if 'message' in stockInfo:
            sendMessage(browser, chatBoxInput,
                        'Ação não encontrada (Somente IBOVESPA aceito)')
            return
        if info == '':
            message = stockToString(stockInfo)
        elif info != '' and info in stockInfo:
            if isinstance(stockInfo[info], (float, int)):
                stockInfo[info] = formatNumber(stockInfo[info])
            message = f' {getKeyDescription(info)}: {stockInfo[info]}'
        else:
            message = f'A info. {info} não foi encontrada'

    else:
        message = f'(BOT) Informar ação. Ex.: !bolsa tots3'

    sendMessage(browser, chatBoxInput, message)


stock_command = {
    'command': '!bolsa', 
    'function': handleStockCommand,
    'args': [],
    'acceptParams': True,
    'description': 'Retorna informações sobre a ação informada no parâmetro.\nSegundo parâmetro é opcional. Ex.: !bolsa tots3 [high]'
}

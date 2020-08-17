from app_util import *
import requests
import re


def findUrls(string):

    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


def handleOutlineCommand(browser, chatBoxInput, link=''):

    links = [link]

    if link == '':
        message = getLastMessageElement(browser, -2)
        links = findUrls(message.text)

    if len(links) == 0:
        sendMessage(browser, chatBoxInput,
                    f'(BOT) Não foi encontrado um link válido')
    else:
        for link in links:
            params = {'source_url': link}
            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'origin': 'https://outline.com',
                'referer': 'https://outline.com/',
            }
            r = requests.get(
                'https://api.outline.com/v3/parse_article', params=params, headers=headers)
            resp = r.json()
            data = resp['data']
            sendMessage(browser, chatBoxInput,
                        f'(BOT) {data["title"]}\n Tempo de leitura de {data["read_time"]}\nhttps://outline.com/{data["short_code"]}')


outline_command = {
    'command': '!xeule',
    'function': handleOutlineCommand,
    'args': [],
    'acceptParams': True,
    'description': 'Remove paywall do ultimo link enviado ou em parametro'
}

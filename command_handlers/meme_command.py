import requests
from app_util import sendMessage


def handleMemeCommand(browser, chatBoxInput):
    r = requests.get('https://meme-api.herokuapp.com/gimme')
    json = r.json()
    sendMessage(browser, chatBoxInput, f'(BOT) {json["title"]} {json["url"]}')


meme_command = {
    'command': '!meme',
    'function': handleMemeCommand,
    'args': [],
    'description': 'Retorna link de um meme do Reddit (EN)'
}

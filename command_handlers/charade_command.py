import requests
import os
import pickle
from app_util import sendMessage

DATA_FILE = '.\datafiles\data.p'


def handleCharadeCommand(browser, chatBoxInput):
    headers = {'Accept': 'application/json'}
    r = requests.get(
        'https://us-central1-kivson.cloudfunctions.net/charada-aleatoria', headers=headers)
    json = r.json()
    sendMessage(browser, chatBoxInput,
                f'(BOT) {json["pergunta"]} (Envie !resposta para ver a resposta)')
    pickle.dump({'lastCharade': json}, open(DATA_FILE, 'wb'))


def handleCharadeAnswerCommand(browser, chatBoxInput):
    if os.path.getsize(DATA_FILE) > 0:
        data = pickle.load(open(DATA_FILE, "rb"))
        if 'lastCharade' in data:
            sendMessage(browser, chatBoxInput,
                        f'(BOT) {data["lastCharade"]["resposta"]} ')
            open(DATA_FILE, 'w').close()


charade_command = {
    'command': '!charada',
    'function': handleCharadeCommand,
    'args': [],
    'description': 'Retorna uma charada bem bosta'
}

charade_answer_command = {
    'command': '!resposta',
    'function': handleCharadeAnswerCommand,
    'args': [],
    'description': 'Retorna a resposta da ultima charada'
}

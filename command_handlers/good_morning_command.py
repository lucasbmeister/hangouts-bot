from app_util import sendMessage


def handleGoodMorningCommand(browser, chatBoxInput, name=''):
    if name != '':
        sendMessage(browser, chatBoxInput, f'(BOT) vai se ferrar {name}')
    else:
        sendMessage(browser, chatBoxInput,
                    f'(BOT) vai se ferrar')


good_morning_command = {
    'command': '!bomdia',
    'function': handleGoodMorningCommand,
    'args': [],
    'acceptParams': True,
    'description': 'Responde bom dia educadamente'
}

import requests
from app_util import sendMessage
from datetime import datetime, timezone, timedelta


def handleNextLaunchCommand(browser, chatBoxInput, provider=''):
    params = {'limit': 1}
    if provider != '':
        params['search'] = provider
    r = requests.get(
        'https://ll.thespacedevs.com/2.0.0/launch/upcoming', params=params)
    launches = r.json()

    if launches['count'] > 0:
        launch = launches['results'][0]

        date = datetime.strptime(launch["net"], '%Y-%m-%dT%H:%M:%SZ')
        date = date - timedelta(hours=3, minutes=0)

        message = '(BOT) Próximo lançamento:\n'
        message += f'{launch["name"]}\n'
        message += f'Data (NET): {date.strftime("%d/%m/%Y %H:%M:%S")}\n'
        message += f'Local: {launch["pad"]["map_url"]}\n'

        if launch['infographic'] != None:
            message += f'Info.: {launch["infographic"]}'
        sendMessage(browser, chatBoxInput, message)
    else:
        sendMessage(browser, chatBoxInput,
                    f'(BOT) Nenhum lançamento encontrado')


next_launch_command = {
    'command': '!lancamento',
    'function': handleNextLaunchCommand,
    'args': [],
    'acceptParams': True,
    'description': 'Próximo lançamento de foguete. Aceita parâmetro. Ex.: !lancamento [spacex]'
}

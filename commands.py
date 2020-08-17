from command_handlers.stock_command import stock_command
from command_handlers.include_command import include_command
from command_handlers.meme_command import meme_command
from command_handlers.charade_command import charade_command, charade_answer_command
from command_handlers.currency_command import dollar_command, euro_command, libra_command, bitcoin_command, currency_command
from command_handlers.translation_command import translation_command
from command_handlers.outline_command import outline_command
from command_handlers.cow_command import cow_command
from command_handlers.next_launch_command import next_launch_command
from command_handlers.covid_command import covid_command
from command_handlers.weather_command import weather_command
from command_handlers.good_morning_command import good_morning_command
from inspect import signature
from app_util import *


def getCleanParams(params):

    cleanParams = []
    indexes = [i for i, x in enumerate(params) if '"' in x]

    if len(indexes) % 2 != 0:
        indexesSingleWords = [i for i, x in enumerate(
            params) if x.startswith('"') and x.endswith('"')]

        if len(indexesSingleWords) > 0 and len(indexesSingleWords) != len(indexes):
            return None

    hasOpenQuote = False
    quotedString = ''
    for string in params:

        if '"' in string:
            hasOpenQuote = not hasOpenQuote

            if not hasOpenQuote or string.startswith('"') and string.endswith('"'):
                cleanParams.append(
                    (quotedString + string).strip().replace('"', ''))
                quotedString = ""
                hasOpenQuote = False
                continue

        if hasOpenQuote:
            quotedString += f'{string} '
        elif not '"' in string and string != ' ':
            cleanParams.append(string)
        pass

    return cleanParams


def handleCommand(browser, chatBoxInput, command, params):

    commandDef = next((x for x in COMMANDS if x['command'] == command), None)

    if commandDef == None:
        return

    function = commandDef['function']
    args = commandDef['args'].copy()

    if commandDef.get('acceptParams', False) and len(params) > 0:
        cleanParams = getCleanParams(params)
        if cleanParams == None:
            sendMessage(browser, chatBoxInput,
                        f'(BOT) Formatação incorreta dos parâmetros')
            return
        args.extend(cleanParams)
    else:
        args.extend(params)

    sig = signature(function)

    if len(sig.parameters) - 2 >= len(args):
        function(browser, chatBoxInput, *args)
    else:
        sendMessage(browser, chatBoxInput,
                    f'(BOT) Número de parâmetros passado incorreto')


def handleCommandList(browser, chatBoxInput):
    commandsList = ' - !entrar : BOT entra no chat\n - !sair : BOT sai do chat\n'
    for command in COMMANDS:
        commandsList += f' - {command["command"]} : {command["description"]} \n'
        pass

    sendMessage(browser, chatBoxInput,
                f'(BOT) Comandos: \n{commandsList}')


command_list_command = {
    'command': '!comandos',
    'function': handleCommandList,
    'args': [],
    'description': 'Retorna esta lista'
}

COMMANDS = [
    stock_command,
    translation_command,
    covid_command,
    outline_command,
    next_launch_command,
    weather_command,
    dollar_command,
    euro_command,
    libra_command,
    bitcoin_command,
    currency_command,
    include_command,
    meme_command,
    charade_command,
    charade_answer_command,
    cow_command,
    good_morning_command,
    command_list_command,
]

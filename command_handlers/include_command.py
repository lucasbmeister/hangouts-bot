from app_util import sendMessage


def handleIncludeCommand(browser, chatBoxInput):
    sendMessage(browser, chatBoxInput,
                f'(BOT) \\\\atusx.engpro.totvs.com.br\Protheus_Data\\temp')


include_command = {
    'command': '!includes',
    'function': handleIncludeCommand,
    'args': [],
    'description': 'Retorna pasta das includes do protheus'
}

from googletrans import Translator, LANGUAGES
from app_util import sendMessage, getLastMessageElement


def handleTranslationCommand(browser, chatBoxInput, text='', languageDest='pt'):

    translator = Translator()
    if text == '':
        lastMessage = getLastMessageElement(browser, -2)
        text = lastMessage.text.replace('(BOT) Tradução:\n', '')

    if text.startswith('!'):
        sendMessage(browser, chatBoxInput, '(BOT) Proibido traduzir comandos')
        return

    if languageDest in LANGUAGES:
        translations = translator.translate([text], dest=languageDest)
    else:
        sendMessage(browser, chatBoxInput, '(BOT) Idioma inválido')
        return

    translatedTexts = ''

    for translation in translations:
        translatedTexts += f'{translation.text}\n'

    sendMessage(browser, chatBoxInput, f'(BOT) Tradução:\n{translatedTexts}')


translation_command = {
    'command': '!traduzir',
    'function': handleTranslationCommand,
    'args': [],
    'acceptParams': True,
    'description': 'Traduz última mensagem enviada ou, o texto em parâmetro.\nIdioma destino é opcional. Ex.: !traduzir Hello [es]'
}

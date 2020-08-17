from app_util import sendMessage


def handleCowCommand(browser, chatBoxInput):
    sendMessage(browser, chatBoxInput,
                '''
         (__)
         (oo)
  /-------\/ 
 / |        ||  
*  ||W---||  
   ^^    ^^  
    ''')


cow_command = {
    'command': '!cow',
    'function': handleCowCommand,
    'args': [],
    'description': 'Mostra uma vaca'
}

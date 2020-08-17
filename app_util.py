import configparser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import threading

SETTINGS_FILE = '.\datafiles\settings.config'


def formatNumber(number):
    if type(number) is int:
        string = f'{number:,}'
        translate = [',', '.']
    else:
        string = f'{number:,.3f}'
        translate = [',.', '.,']

    maketrans = string.maketrans

    return string.translate(maketrans(*translate))


def sendMessage(browser, chatBoxInput, message):
    lock = threading.Lock()

    with lock:
        chatBoxInput.click()

        lines = message.split('\n')
        for line in lines:
            chatBoxInput.send_keys(line)
            ActionChains(browser).key_down(Keys.SHIFT).key_down(
                Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()
            pass

        chatBoxInput.send_keys(Keys.RETURN)


def getLastMessageElement(browser, lastIndex=-1):
    messageElements = browser.find_elements_by_css_selector(
        "span[class='tL8wMe EMoHub']")
    return messageElements[lastIndex]


def setConfig(section, key, value):
    parser = configparser.ConfigParser()
    parser.read(SETTINGS_FILE, encoding='utf-8')
    parser.set(section, key, value)

    with open(SETTINGS_FILE, 'wb') as configfile:
        parser.write(configfile)


def getConfig(section, key=''):
    parser = configparser.ConfigParser()
    parser.read(SETTINGS_FILE, encoding='utf-8')
    if key != '':
        setting = parser[section][key]
    else:
        setting = parser[section]
    return setting

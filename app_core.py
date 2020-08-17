from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import threading
from commands import *
from app_util import *

bot_connected = False

def handleBotConnection(browser, chatBoxInput, command):
    global bot_connected
    if bot_connected and '!sair' in command:
        bot_connected = False
        sendMessage(browser, chatBoxInput, '(BOT) Saindo do chat')
    elif not bot_connected and '!entrar' in command:
        bot_connected = True
        sendMessage(browser, chatBoxInput, '(BOT) Entrando do chat')


def executeCommand(browser, chatBoxInput, command):
    params = command.split(' ')
    t = threading.Thread(target=handleCommand, args=(
        browser, chatBoxInput, params[0], params[1:]))
    t.start()
    t.join()
    #handleCommand(browser, chatBoxInput, params[0], params[1:])


def runBot(chatName):

    global bot_connected

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=selenium")

    browser = webdriver.Chrome(
        ".\chromedriver_win32\chromedriver.exe", options=chrome_options)

    browser.get("https://hangouts.google.com/")

    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "iframe[aria-label='Contatos e conversas']")))
        iframe = browser.find_element_by_css_selector(
            "iframe[aria-label='Contatos e conversas']")
        browser.switch_to_frame(iframe)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[text() = '" + chatName + "']")))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    chat = browser.find_element(
        By.XPATH, "//div[text() = '" + chatName + "']")
    chat.click()
    browser.switch_to.default_content()

    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "iframe[aria-label='" + chatName + "']")))
        iframe = browser.find_element_by_css_selector(
            "iframe[aria-label='" + chatName + "']")
        browser.switch_to_frame(iframe)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[aria-label=' Campo de entrada de texto para " + chatName + ".  O histórico está ativado. ']")))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    chatBoxInput = browser.find_element_by_css_selector(
        "div[aria-label=' Campo de entrada de texto para " + chatName + ".  O histórico está ativado. ']")

    while True:
        lastMessage = getLastMessageElement(browser)
        command = lastMessage.text
        if command.startswith('!'):
            if '!entrar' in command or '!sair' in command:
                handleBotConnection(browser, chatBoxInput, command)
            elif bot_connected:
                executeCommand(browser, chatBoxInput, command)
            pass
        pass


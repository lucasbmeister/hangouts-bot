import app_core
from app_util import getConfig

chat = getConfig('CONFIG', 'chat')
app_core.runBot(chat)

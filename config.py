import os
from os import environ

class Config:
    API_ID = 26229903
    API_HASH = "b5197d148bd3665a1eb45d1d18b02ad3"
    BOT_TOKEN = "6737484095:AAHp5AsBUmmnZvZlsaJMkK3kMa4S5A0ahx0"
    BOT_SESSION = environ.get("BOT_SESSION", "bot")
    DATABASE_URI = "mongodb+srv://Erichdaniken:Erichdaniken@cluster0.ldsblpl.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_NAME = "Cluster0"
    BOT_OWNER_ID = 503170505

class temp(object):
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

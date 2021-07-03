from configparser import ConfigParser

config = ConfigParser()

config.read("settings.ini")

settings = {
    'token': config.get("BOT", "token"),
    'id': config.get("BOT", "clientid"),
    'adminid': config.get("BOT", "adminid"),
    'prefix': config.get("BOT", "prefix"),
    'status': config.get("BOT", "status"),
    'playing': config.get("BOT", "playing"),
}

language = config.get("LOCALE", "language")
section = language.upper()
config.read("locales/{}.ini".format(language))

lang = {
    'cogunload': config.get(section, "cogunload"),
    'cogload': config.get(section, "cogload"),
    'notenoughrights': config.get(section, "notenoughrights"),
    'cogreload': config.get(section, "cogreload"), 
    'congrats': config.get(section, "congrats"), 
    'lvlup': config.get(section, "lvlup"), 
    'notpoll': config.get(section, "notpoll"), 
    'newpoll': config.get(section, "newpoll"), 
    'pollgivenby': config.get(section, "pollgivenby"), 
}
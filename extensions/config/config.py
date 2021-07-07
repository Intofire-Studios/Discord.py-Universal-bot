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
    'login': config.get(section, "login"),
    'prefix': config.get(section, "prefix"),
    'status': config.get(section, "status"),
    'playing': config.get(section, "playing"),
    'cogunload': config.get(section, "cogunload"),
    'cogload': config.get(section, "cogload"),
    'notenoughrights': config.get(section, "notenoughrights"),
    'cogreload': config.get(section, "cogreload"), 
    'congrats': config.get(section, "congrats"), 
    'lvlup': config.get(section, "lvlup"), 
    'notpoll': config.get(section, "notpoll"), 
    'newpoll': config.get(section, "newpoll"), 
    'pollgivenby': config.get(section, "pollgivenby"), 
    'hello': config.get(section, "hello"), 
    'shutdown': config.get(section, "shutdown"), 
    'latency': config.get(section, "latency"), 
    'response': config.get(section, "response"), 
    'avatar': config.get(section, "avatar"), 
    'fox': config.get(section, "fox"), 
    'cat': config.get(section, "cat"), 
    'kickby': config.get(section, "kickby"), 
    'banby': config.get(section, "banby"), 
    'unbanby': config.get(section, "unbanby"), 
    'msgdelete': config.get(section, "msgdelete"), 
    'errorblock': config.get(section, "errorblock"), 
    'cmdnotfound': config.get(section, "cmdnotfound"),
    'msgcmdnotfound': config.get(section, "msgcmdnotfound"),
    'slowmodeerror': config.get(section, "slowmodeerror"), 
    'msgslowmodeerror': config.get(section, "msgslowmodeerror"), 
    'missingpermissions': config.get(section, "missingpermissions"), 
    'msgmissingpermissions': config.get(section, "msgmissingpermissions"),
    'missingarguments': config.get(section, "missingarguments"), 
    'msgmissingarguments': config.get(section, "msgmissingarguments"), 
    'notvoice': config.get(section, "notvoice"),
    'msgnotvoice': config.get(section, "msgnotvoice"),
    'nowplaying': config.get(section, "nowplaying"),
    'duration': config.get(section, "duration"),
    'reqby': config.get(section, "reqby"),
    'uploader': config.get(section, "uploader"),
    'url': config.get(section, "url"),
    'track': config.get(section, "track"),
    'trackadded': config.get(section, "trackadded"),
    'togo': config.get(section, "togo"),
    'queue': config.get(section, "queue"),
    'notplaying': config.get(section, "notplaying"),
    'pause': config.get(section, "pause"),
    'resume': config.get(section, "resume"),
    'notconnected': config.get(section, "notconnected"),
    'skip': config.get(section, "skip"),
}
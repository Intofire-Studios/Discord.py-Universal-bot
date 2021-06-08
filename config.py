from configparser import ConfigParser

config = ConfigParser()
path = "settings.ini"

config.read("settings.ini")

settings = {
    'token': config.get("BOT","token"),
    'id': config.get("BOT","clientid"),
    'adminid': config.get("BOT","adminid"),
    'prefix': config.get("BOT","prefix")
}
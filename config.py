from configparser import ConfigParser

config = ConfigParser()
path = "settings.ini"

config.read("settings.ini")

settings = {
    'token': config.get("BOT","token"),
    'id': config.get("BOT","clientid"),
    'prefix': config.get("BOT","prefix")
}
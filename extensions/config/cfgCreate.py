from configparser import ConfigParser
from os import system

config = ConfigParser()
path = "settings.ini"


def cfgcreate(path):
    config.add_section("BOT")
    config.set("BOT", "token", input("\033[31m {}" .format("Enter bot token:") + "\033[0m "))
    config.set("BOT", "clientid", input("\033[31m {}" .format("Enter ClientID:") + "\033[0m "))
    config.set("BOT", "adminid", input("\033[31m {}" .format("Enter your Discord ID:") + "\033[0m "))
    config.set("BOT", "prefix", input("\033[31m {}" .format("Enter bot prefix:") + "\033[0m "))
    with open(path, "w+") as config_file:
        path = "settings.ini"
        config.write(config_file)
    system("cls")
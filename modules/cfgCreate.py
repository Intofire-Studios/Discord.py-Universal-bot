from configparser import ConfigParser
from os import system

config = ConfigParser()

path = "settings.ini"

def cfgCreate(path):
    config.add_section("BOT")
    config.set("BOT", "token", input("Enter bot token: "))
    config.set("BOT", "name", input("Enter bot name: "))
    config.set("BOT", "clientid", input("Enter ClientID: "))
    config.set("BOT", "prefix", input("Enter bot prefix: "))
    
    with open(path, "w+") as config_file:
        path = "settings.ini"
        config.write(config_file)
    
    system("cls")

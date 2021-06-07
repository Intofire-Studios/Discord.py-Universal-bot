from configparser import ConfigParser

config = ConfigParser()

path = "settings.ini"

def cfgCreate(path):
    config.add_section("BOT")
    print("Enter bot token: ")
    config.set("BOT", "token", input())
    print("Enter bot name: ")
    config.set("BOT", "name", input())
    print("Enter ClientID: ")
    config.set("BOT", "clientid", input())
    print("Enter bot prefix: ")
    config.set("BOT", "prefix", input())
    
    with open(path, "w+") as config_file:
        path = "settings.ini"
        config.write(config_file)

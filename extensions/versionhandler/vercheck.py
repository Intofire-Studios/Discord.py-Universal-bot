from os import system
from time import sleep
from sys import platform
def update():
    system("git pull")
    sleep(3)
    if platform in ["linux", "linux2"]:
        system("reset")
    elif platform == "win32":
        system("cls") 
    sleep(3) 
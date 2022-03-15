from rich.console import Console
from rich.theme import Theme
import pydirectinput as pdi
from time import sleep
from PIL import Image
import webbrowser
import pyautogui
import requests
import psutil
import os

theme = Theme({"success": "green", "error": "bold red1", "process": "blue"})
console = Console(theme=theme)

pdi.FAILSAFE = False

class Bot:
    def __init__(self):
        self.logo = """
         ██████╗██╗     ██╗   ██╗███████╗████████╗███████╗██████╗ ███╗   ██╗ ██████╗ ██╗    ██╗███╗   ██╗
        ██╔════╝██║     ██║   ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔═══██╗██║    ██║████╗  ██║
        ██║     ██║     ██║   ██║███████╗   ██║   █████╗  ██████╔╝██╔██╗ ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
        ██║     ██║     ██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██║   ██║██║███╗██║██║╚██╗██║
        ╚██████╗███████╗╚██████╔╝███████║   ██║   ███████╗██║  ██║██║ ╚████║╚██████╔╝╚███╔███╔╝██║ ╚████║
         ╚═════╝╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝"""
        self.author = 'RTxNINJA'
        self.version = '2.8.0'

        self.playImage = Image.open(requests.get("", stream=True).raw)
        self.trainingImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Training.png", stream=True).raw)
        self.loneWolfImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Lone-Wolf.png", stream=True).raw)
        self.locationsImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Locations.png", stream=True).raw)
        self.operatorsImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Operators.png", stream=True).raw)
        self.loadoutImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Loadout.png", stream=True).raw)
        self.retryImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Retry.png", stream=True).raw)

    def openR6(self):
        pass
        webbrowser.open_new_tab("steam://rungameid/359550")
        
    def isR6Running(self):
        if "RainbowSix.exe" in (p.name() for p in psutil.process_iter()):
            os.system("taskkill /f /im RainbowSix.exe")
        console.clear()
        sleep(5)
        self.openR6()

    def welcomeScreen(self):
        console.print(self.logo, style="bold gold3", justify="center")
        console.print(f"Author: {self.author}", style="purple3", justify="center")
        console.print(f"Version: {self.version}", style="turquoise2", justify="center")
        console.print()

    def findImage(self, image):
        console.print(f"Looking for {image} button...", style="process")
        for i in range(300):
            if pyautogui.locateOnScreen(image, confidence=0.6):
                console.print(f"Found {image} button!", style="success")
                print()
                return
            else:
                sleep(0.5)

    def enterMatch(self):
        self.findImage(self.playImage)
        sleep(3)
        pdi.press("left")
        sleep(0.25)
        pdi.press("enter")

        self.findImage(self.trainingImage)
        sleep(1)
        pdi.press("left")
        sleep(0.25)
        pdi.press("enter")
        sleep(1)

        self.findImage(self.loneWolfImage)
        sleep(1)
        pdi.press("f")
        sleep(0.25)
        pdi.press("f")
        sleep(0.25)
        pdi.press("left")
        sleep(0.25)
        pdi.press("enter")
        sleep(1)
    
    def preMatchConfig(self):
        self.findImage(self.locationsImage)
        sleep(1)
        pdi.press("down")
        sleep(0.25)
        pdi.press("enter")

        self.findImage(self.operatorsImage)
        sleep(1)
        pdi.press("down")
        sleep(0.25)
        pdi.press("right")
        sleep(0.25)
        pdi.press("right")
        sleep(0.25)
        pdi.press("right")
        sleep(0.25)
        pdi.press("right")
        sleep(0.25)
        pdi.press("enter")

        self.findImage(self.loadoutImage)
        sleep(1)
        pdi.press("enter")
        
    def retryMatch(self):
        self.findImage(self.retryImage)
        sleep(1)
        pdi.press("enter")

    def run(self):
        self.preMatchConfig()
        self.retryMatch()

def main():
    bot = Bot()
    bot.isR6Running()
    bot.welcomeScreen()
    bot.enterMatch()

    while True:
        bot.run()

if __name__ == "__main__":
    try:
        main()
    except:
        pass

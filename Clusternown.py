from rich.console import Console
from rich.theme import Theme
import pydirectinput as pdi
from PIL import Image
import webbrowser
import pyautogui
import requests
import psutil
import time
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
        self.version = '3.0'

        self.consoleSize = os.get_terminal_size()

        self.playImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Play.png", stream=True).raw)
        self.trainingImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Training.png", stream=True).raw)
        self.loneWolfImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Lone-Wolf.png", stream=True).raw)
        self.locationsImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Locations.png", stream=True).raw)
        self.operatorsImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Operators.png", stream=True).raw)
        self.loadoutImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Loadout.png", stream=True).raw)
        self.retryImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/Clusternown/master/assets/Retry.png", stream=True).raw)

    def openR6(self):
        webbrowser.open_new_tab("steam://rungameid/359550")
        
    def isR6Running(self):
        if "RainbowSix.exe" in (p.name() for p in psutil.process_iter()):
            os.system("taskkill /f /im RainbowSix.exe")

        console.clear()
        time.sleep(5)
        self.openR6()

    def welcomeScreen(self):
        console.print(self.logo, style="bold gold3", justify="center")
        console.print(f"Author: {self.author}", style="purple3", justify="center")
        console.print(f"Version: {self.version}", style="turquoise2", justify="center")
        console.print()

    def findImage(self, image, imageName):
        lookingForImage = f"[-] LOOKING FOR {imageName.upper()} BUTTON..."
        foundImage = f"[✓] FOUND {imageName.upper()} BUTTON!"
        currentTime = f"{time.strftime('%I:%M %p', time.localtime())}]"
        lookingForImagePadding = self.consoleSize.columns - len(lookingForImage) -  len(currentTime)
        foundImagePadding = self.consoleSize.columns - len(foundImage) -  len(currentTime)

        console.print(f"{lookingForImage}{'[':>{lookingForImagePadding}}{currentTime}", style="process")
        for i in range(300):
            if pyautogui.locateOnScreen(image, confidence=0.6):
                console.print(f"{foundImage}{'[':>{foundImagePadding}}{currentTime}", style="success")

                print()
                return
            else:
                time.sleep(0.5)

    def enterMatch(self):
        self.findImage(self.playImage, 'Play')
        time.sleep(3)
        pdi.press("enter")

        self.findImage(self.trainingImage, 'Training')
        time.sleep(1)
        pdi.press("left")
        time.sleep(0.25)
        pdi.press("enter")
        time.sleep(1)

        self.findImage(self.loneWolfImage, 'Lone Wolf')
        time.sleep(1)
        pdi.press("f")
        time.sleep(0.25)
        pdi.press("f")
        time.sleep(0.25)
        pdi.press("left")
        time.sleep(0.25)
        pdi.press("enter")
        time.sleep(1)
    
    def preMatchConfig(self):
        self.findImage(self.locationsImage, 'Locations')
        time.sleep(1)
        pdi.press("down")
        time.sleep(0.25)
        pdi.press("enter")

        self.findImage(self.operatorsImage, 'Operators')
        time.sleep(1)
        pdi.press("down")
        time.sleep(0.25)
        pdi.press("right")
        time.sleep(0.25)
        pdi.press("right")
        time.sleep(0.25)
        pdi.press("right")
        time.sleep(0.25)
        pdi.press("right")
        time.sleep(0.25)
        pdi.press("enter")

        self.findImage(self.loadoutImage, 'Loadout')
        time.sleep(1)
        pdi.press("enter")
        
    def retryMatch(self):
        self.findImage(self.retryImage, 'Retry')
        time.sleep(1)
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

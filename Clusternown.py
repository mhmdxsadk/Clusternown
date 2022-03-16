from rich.console import Console
from rich.theme import Theme
import pydirectinput as pdi
from PIL import Image
import webbrowser
import subprocess
import pyautogui
import requests
import hashlib 
import psutil
import time
import json
import os

theme = Theme({"success": "green", "error": "bold red1", "process": "blue"})
console = Console(theme=theme)

pdi.FAILSAFE = False
pyautogui.FAILSAFE = False
class Bot:
    def __init__(self):
        self.logo = """
         ██████╗██╗     ██╗   ██╗███████╗████████╗███████╗██████╗ ███╗   ██╗ ██████╗ ██╗    ██╗███╗   ██╗
        ██╔════╝██║     ██║   ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔═══██╗██║    ██║████╗  ██║
        ██║     ██║     ██║   ██║███████╗   ██║   █████╗  ██████╔╝██╔██╗ ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
        ██║     ██║     ██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██║   ██║██║███╗██║██║╚██╗██║
        ╚██████╗███████╗╚██████╔╝███████║   ██║   ███████╗██║  ██║██║ ╚████║╚██████╔╝╚███╔███╔╝██║ ╚████║
         ╚═════╝╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝"""
        self.author = 'IQ.EXE#7301'
        self.version = '4.2.1'

        self.consoleSize = os.get_terminal_size()

        self.playImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/ClusternownAssets/master/assets/Play.png", stream=True).raw)
        self.trainingImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/ClusternownAssets/master/assets/Training.png", stream=True).raw)
        self.loneWolfImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/ClusternownAssets/master/assets/Lone-Wolf.png", stream=True).raw)
        self.locationsImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/ClusternownAssets/master/assets/Locations.png", stream=True).raw)
        self.operatorsImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/ClusternownAssets/master/assets/Operators.png", stream=True).raw)
        self.loadoutImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/ClusternownAssets/master/assets/Loadout.png", stream=True).raw)
        self.retryImage = Image.open(requests.get("https://raw.githubusercontent.com/RTxNINJA/ClusternownAssets/master/assets/Retry.png", stream=True).raw)

        self.hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        self.hashedHwid = hashlib.sha256(str.encode(self.hwid)).hexdigest()
        self.r = requests.get('https://rentry.co/HspwiEqGlEuk8VS8L0WSJFpf5HGg5TVnAZ5bhpSkxa9rwzc7PTwSvGb3Iq053jVuDJvHdfL0BFteUTZI/raw')
        self.hwidList = str(self.r.text)
        self.jsonHwidList = json.loads(self.hwidList)

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
        time.sleep(2)
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

bot = Bot()
start = time.time()
roundCounter = 0
if bot.hashedHwid in bot.jsonHwidList["HWID"]:
    bot.isR6Running()
    bot.welcomeScreen()
    bot.enterMatch()
    try:
        while True:
            roundCounter += 1
            console.print(f"---------- [Round:{roundCounter}] ----------", style="dark_cyan")
            bot.run()
            console.print("", style="")
    except KeyboardInterrupt:
        end = time.time()

    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    console.print(f"\nElapsed time: {int(hours):0>2}:{int(minutes):0>2}:{seconds:0>5.2f}", style="purple3")
else:
    console.print("YOU ARE NOT WHITELISTED", style='error')

console.input('Press any key to continue...')

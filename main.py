from subprocess import check_output, check_call, DEVNULL, STDOUT
from rich.console import Console
from rich.theme import Theme
import pydirectinput as pdi
from PIL import Image
import webbrowser
import pyautogui
import requests
import hashlib
import psutil
import time
import json

theme = Theme(
    {"success": "green1", "error": "bold red1", "process": "dark_slate_gray2"}
)
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
        self.version = "5.0.0"

        self.playImage = Image.open(
            requests.get(
                "https://raw.githubusercontent.com/moealkurdi/ClusternownAssets/master/assets/Play.png",
                stream=True,
            ).raw
        )
        self.trainingImage = Image.open(
            requests.get(
                "https://raw.githubusercontent.com/moealkurdi/ClusternownAssets/master/assets/Training.png",
                stream=True,
            ).raw
        )
        self.loneWolfImage = Image.open(
            requests.get(
                "https://raw.githubusercontent.com/moealkurdi/ClusternownAssets/master/assets/Lone-Wolf.png",
                stream=True,
            ).raw
        )
        self.locationsImage = Image.open(
            requests.get(
                "https://raw.githubusercontent.com/moealkurdi/ClusternownAssets/master/assets/Locations.png",
                stream=True,
            ).raw
        )
        self.operatorsImage = Image.open(
            requests.get(
                "https://raw.githubusercontent.com/moealkurdi/ClusternownAssets/master/assets/Operators.png",
                stream=True,
            ).raw
        )
        self.loadoutImage = Image.open(
            requests.get(
                "https://raw.githubusercontent.com/moealkurdi/ClusternownAssets/master/assets/Loadout.png",
                stream=True,
            ).raw
        )
        self.retryImage = Image.open(
            requests.get(
                "https://raw.githubusercontent.com/moealkurdi/ClusternownAssets/master/assets/Retry.png",
                stream=True,
            ).raw
        )

        self.hwid = (
            check_output("wmic csproduct get uuid").decode().split("\n")[1].strip()
        )
        self.hashedHwid = hashlib.sha256(str.encode(self.hwid)).hexdigest()
        self.r = requests.get(
            "https://rentry.co/HspwiEqGlEuk8VS8L0WSJFpf5HGg5TVnAZ5bhpSkxa9rwzc7PTwSvGb3Iq053jVuDJvHdfL0BFteUTZI/raw"
        )
        self.userInfo = str(self.r.text)
        self.jsonUserInfo = json.loads(self.userInfo)

        self.hwidIndex = 0
        for i, j in enumerate(self.jsonUserInfo):
            if j["HWID"] == self.hashedHwid:
                self.hwidIndex = i

    def openR6(self):
        if "RainbowSix.exe" in (p.name() for p in psutil.process_iter()):
            check_call("taskkill /F /IM RainbowSix.exe", stdout=DEVNULL, stderr=STDOUT)
            time.sleep(5)
        if "Steam" in self.jsonUserInfo[self.hwidIndex]["Platform"]:
            webbrowser.open_new_tab("steam://rungameid/359550")

        elif "Ubisoft" in self.jsonUserInfo[self.hwidIndex]["Platform"]:
            webbrowser.open_new_tab("uplay://launch/1842/0")

    def welcomeScreen(self):
        console.print(self.logo, style="bold gold1", justify="center")
        console.print(
            f"Version: {self.version}",
            style="turquoise2",
            justify="center",
            highlight=False,
        )

    def findImage(self, image, imageName):
        lookingForImage = f"[-] LOOKING FOR {imageName.upper()} BUTTON..."
        foundImage = f"[-] FOUND {imageName.upper()} BUTTON!"

        console.print(f"\n{lookingForImage}", style="process", highlight=False)
        for i in range(300):
            if pyautogui.locateOnScreen(image, confidence=0.6):
                console.print(f"{foundImage}\n", style="success", highlight=False)
                return
            else:
                time.sleep(0.5)

    def enterMatch(self):
        self.findImage(self.playImage, "Play")
        time.sleep(1)
        pdi.press("enter")

        self.findImage(self.trainingImage, "Training")
        time.sleep(1)
        pdi.press("left")
        time.sleep(0.25)
        pdi.press("enter")

        self.findImage(self.loneWolfImage, "Lone Wolf")
        time.sleep(1)
        pdi.press("f")
        time.sleep(0.25)
        pdi.press("f")
        time.sleep(0.25)
        pdi.press("left")
        time.sleep(0.25)
        pdi.press("enter")

    def preMatchConfig(self):
        self.findImage(self.locationsImage, "Locations")
        time.sleep(1)
        pdi.press("down")
        time.sleep(0.25)
        pdi.press("enter")

        self.findImage(self.operatorsImage, "Operators")
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

        self.findImage(self.loadoutImage, "Loadout")
        time.sleep(1)
        pdi.press("enter")

    def retryMatch(self):
        self.findImage(self.retryImage, "Retry")
        time.sleep(1)
        pdi.press("enter")

    def run(self):
        self.preMatchConfig()
        self.retryMatch()


console.clear()
bot = Bot()
roundCounter = 0
if bot.hashedHwid in bot.jsonUserInfo[bot.hwidIndex]["HWID"]:
    bot.welcomeScreen()
    bot.openR6()
    start = time.time()
    bot.enterMatch()
    try:
        while True:
            roundCounter += 1
            console.print(
                f"---------- [Round:{roundCounter}] ----------",
                style="blue_violet",
                highlight=False,
            )
            bot.run()
    except KeyboardInterrupt:
        end = time.time()

    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    console.print(
        f"\nElapsed time: {int(hours):0>2}:{int(minutes):0>2}:{seconds:0>5.2f}",
        style="blue_violet",
        highlight=False,
    )
else:
    console.print("YOU ARE NOT WHITELISTED", style="error", highlight=False)

console.input("Press any key to continue...")

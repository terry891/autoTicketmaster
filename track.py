import macmouse as mouse
import time
import random
import os
import threading
from PIL import ImageGrab
from pynput.keyboard import Key, Controller


class Track:
    def __init__(self) -> None:
        self.mouse = mouse
        self.keyboard = Controller()
        self.ColorQueue = (34, 34, 34, 255)
        self.ColorTicket = (228, 233, 240, 255)

    def checkStart(self) -> None:
        start = ""
        while start != "y":
            start = input("Get Taylor Swift Ticket?? (y/n): ")
            if start == "n":
                print("Sad sad sad")
                quit()

    def checkPixel(self, x, y):
        im = ImageGrab.grab()
        pix = im.load()
        self.move(x, y)
        return pix[x, y]

    def enterString(self, info) -> None:
        for character in info:
            self.keyboard.press(character)
            self.keyboard.release(character)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        # self.keyboard.press(Key.enter)
        # self.keyboard.release(Key.enter)

    def getTicket(self):
        thread = threading.Thread(target=self.alert)
        thread.start()

        # Get first ticket
        self.move(1859, 457)
        self.mouse.click(button="left")
        time.sleep(0.4)

        # Click NEXT
        self.move(1714, 1046)
        self.mouse.click(button="left")
        self.mouse.click(button="left")
        time.sleep(4.5)

        # Check agreement terms
        self.move(1104, 527)
        self.mouse.click(button="left")
        time.sleep(2)

        # Enter CSV
        self.move(580, 612)
        time.sleep(0.5)
        self.mouse.click(button="left")
        self.enterString("135")
        time.sleep(0.5)
        
        # Place order
        self.move(1269, 589)        
        thread.join() 

    def alert(self):
        duration = 0.4
        freq = 1760
        os.system('sox -q -r 48000 -n -b 16 -c 2 tem.wav synth {} sin {} vol -10dB &>/dev/null'.format(duration, freq))
        for _ in range(3):
            os.system('play tem.wav &>/dev/null')
            time.sleep(0.1)
        os.system('say "Mei Mei ticket is ready!"')
        os.system('rm tem.wav')

    def refreshTab(self):
        self.move(1339, 27)
        time.sleep(0.1)
        self.mouse.click(button="left")

    def move(self, x, y) -> None:
        duration = random.randint(20, 50) / 1000
        self.mouse.move(x, y, absolute=True, duration=duration)
        # self.mouse.move(700,700)
    
    def click(self, button) -> None:
        self.mouse.click(button=button)

def testKeyboard():
    track = Track()
    time.sleep(2)
    track.move(1012, 19)
    track.click("left")
    track.enterString("https://we-ha.com/wp-content/uploads/2019/09/4D456B73-A8A4-40FA-BE21-62F4C87D4188-810x586.jpg")

def testPixel():
    track = Track()
    time.sleep(2)
    track.checkPixel(1407, 264)

# testKeyboard()
# testPixel()


if __name__ == '__main__':
    # track.checkStart()
    track = Track()
    time.sleep(2)

    while(True):
        check_color = track.checkPixel(1407, 264)
        if check_color == track.ColorQueue:
            delay = random.randint(100, 500) / 100
            time.sleep(delay)
            track.refreshTab()
        elif check_color == track.ColorTicket:
            track.getTicket()
            break
    

        
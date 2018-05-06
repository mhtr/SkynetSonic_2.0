import win32gui
import pyautogui
from PIL import ImageGrab
from tkinter import Canvas, Tk, Text
from PIL import ImageTk
import search


def setFocus(name):
    handle = win32gui.FindWindow(name, None)
    win32gui.SetForegroundWindow(handle)


def printScr():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('prtsc')
    pyautogui.keyUp('prtsc')
    pyautogui.keyUp('alt')
    return ImageGrab.grabclipboard()


class Redraw:
    def __init__(self, img):
        self.width = img.width
        self.height = img.height
        self.root = Tk()
        self.root.geometry('{}x{}'.format(self.width, self.height + 50))
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        image = ImageTk.PhotoImage(img)
        self.imgarea = self.canvas.create_image(self.width / 2, self.height / 2, image=image)
        self.tx = Text(font=('times', 12), width=50, height=15)
        self.tx.pack()



    def updateImage(self, img):
        image = ImageTk.PhotoImage(img[0])
        self.canvas.itemconfig(self.imgarea, image=image)
        self.tx.insert(1.0, '{}\n{}\n'.format(img[1], img[2]))
        self.root.update()
        #self.root.mainloop()

    def mainLoop(self):
        while True:
            self.canvas.after(0, self.updateImage(search.search()))

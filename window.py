import win32gui
import pyautogui
from PIL import ImageGrab
from tkinter import Canvas, Tk
from PIL import ImageTk


def setFocus(name):
    handle = win32gui.FindWindow(name, None)
    win32gui.SetForegroundWindow(handle)


def printScr():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('prtsc')
    pyautogui.keyUp('prtsc')
    pyautogui.keyUp('alt')
    return ImageGrab.grabclipboard()


def createWindow(img):
    width = img.width
    height = img.height
    root = Tk()
    root.geometry('{}x{}'.format(width, height))
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    image = ImageTk.PhotoImage(img)
    canvas.create_image(width / 2, height / 2, image=image)
    root.mainloop()
import pyautogui
import time

def goForward():
    pyautogui.keyDown('d')


def stopForward():
    pyautogui.keyUp('d')


def goBackward():
    pyautogui.keyDown('a')


def stopBackward():
    pyautogui.keyUp('a')


def jump():

    pyautogui.keyDown('k')
    #time.sleep()
    pyautogui.keyUp('k')

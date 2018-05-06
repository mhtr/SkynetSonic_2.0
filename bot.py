import window
import const
import mrrobot
import search

window.setFocus(const.NAME_OF_WINDOW)
#mrrobot.jump()
screened_img = window.printScr()
rdrw = window.Redraw(screened_img)
rdrw.mainLoop()
import window
import const
import mrrobot
from PIL import Image, ImageDraw

testimg = Image.open('Images/1_.jpg')
window.setFocus(const.NAME_OF_WINDOW)
img = window.printScr()
mrrobot.jump()

window.createWindow(img)

widthBig = img.size[0]
heightBig = img.size[1]

width = testimg.size[0] #Определяем ширину.
height = testimg.size[1]
bigPix = img.load()
pix = testimg.load()


print(testimg.size)
flag = False
for bigpixel in range(250, widthBig - width - 200):
    for bigpixel2 in range(250, heightBig - height):

        n = 0
        n1 = 0
        print('Search in: {}:{}'.format(bigpixel, bigpixel2))
        for pixel in range(width):
            for pixel2 in range(height):
                n= n + 1
                a, b, c = pix[pixel, pixel2]
                big_a, big_b, big_c = bigPix[bigpixel + pixel, bigpixel2 + pixel2]

                if (a > 12 and b > 140 or b < 130 and c > 240 or c < 230):
                    #print('Search in: {}:{}'.format(widthBig, heightBig))
                    if ((a > (big_a - 10) and a < (big_a + 10)) and (b > (big_b - 10) and b < (big_b + 10)) and (c > (big_c - 10) and c < (big_c + 10))):
                        n1 = n1 + 1
        print('{}'.format(n1))
        if (float(n1) / float(n) > 0.1):
            print('Succefull {}, {}'.format(widthBig, heightBig))
            flag = True
            break
    if (flag):
        break


print('{}: {}'.format(n, n1))
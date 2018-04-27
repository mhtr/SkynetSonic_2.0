import window
import const
import mrrobot
from PIL import Image, ImageDraw
import time
sprites = ['spr_main', 'spr_wait', 'spr_run_1', 'spr_run_2', 'spr_jump_1', 'spr_jump_2', 'spr_fail_1', 'spr_fail_2']
sprite = []
for spr in sprites:
    sprite.append(Image.open('Images/Sonic/{}.jpg'.format(spr)))

window.setFocus(const.NAME_OF_WINDOW)
img = window.printScr()
detected = ImageDraw.Draw(img)

mrrobot.jump()

widthBig = img.size[0]
heightBig = img.size[1]

width = sprite.size[0]
height = sprite.size[1]
bigPix = img.load()
pix = sprite.load()

print(sprite.size)
flag = False
a = time.clock()
for bigpixel in range(0, widthBig - width - 200, 8):
    for bigpixel2 in range(0, heightBig - height, 8):

        n = 0
        n1 = 0

        print('Search in: {}:{}'.format(bigpixel, bigpixel2))
        for pixel in range(0, width, 4):
            for pixel2 in range(0, height, 4):
                n = n + 1
                a, b, c = pix[pixel, pixel2]
                big_a, big_b, big_c = bigPix[bigpixel + pixel, bigpixel2 + pixel2]

                if (a > 12 and b > 140 or b < 130 and c > 240 or c < 230):

                    if (((big_a - 10) < a < (big_a + 10)) and ((big_b - 10) < b < (big_b + 10)) and (
                            (big_c - 10) < c < (big_c + 10))):
                        n1 = n1 + 1
        print('{}'.format(n1))
        if float(n1) / float(n) > 0.12:
            print('Succefull {}, {}'.format(bigpixel, bigpixel2))
            detected.rectangle((bigpixel, bigpixel2, width + bigpixel, height + bigpixel2), outline='red')
            print(time.clock())
            flag = True
            break
    if flag:
        break

window.createWindow(img)
print('{}: {}'.format(n, n1))

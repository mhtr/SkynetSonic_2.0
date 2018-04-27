import window
from PIL import Image, ImageDraw
import time


def search():
    sprite_list = ['spr_main',
                   'spr_wait',
                   'spr_run_1',
                   'spr_run_2',
                   'spr_jump_1',
                   'spr_jump_2',
                   'spr_fail_1',
                   'spr_fail_2'
                   ]
    sprite = []
    for spr in sprite_list:
        sprite.append(Image.open('Images/Sonic/{}.jpg'.format(spr)))

    screened_img = window.printScr()
    detected = ImageDraw.Draw(screened_img)

    screened_img_width = screened_img.size[0]
    screened_img_height = screened_img.size[1]

    bigPix = screened_img.load()

    print(sprite[0].size)
    flag = False
    a = time.clock()
    for spr in sprite:
        sprite_width = spr.size[0]
        sprite_height = spr.size[1]
        pix = spr.load()
        for screened_img_pixel_w in range(0, screened_img_width - sprite_width - 200, 8):
            for screened_img_pixel_h in range(0, screened_img_height - sprite_height, 8):

                total_pixel = 0
                found_pixel = 0

                print('Search in: {}:{}'.format(screened_img_pixel_w, screened_img_pixel_h))
                for sprite_pixel_w in range(0, sprite_width, 4):
                    for sprite_pixel_h in range(0, sprite_height, 4):
                        total_pixel = total_pixel + 1
                        a, b, c = pix[sprite_pixel_w, sprite_pixel_h]
                        big_a, big_b, big_c = bigPix[
                            screened_img_pixel_w + sprite_pixel_w, screened_img_pixel_h + sprite_pixel_h]

                        if (a > 12 and b > 140 or b < 130 and c > 240 or c < 230):

                            if (((big_a - 10) < a < (big_a + 10)) and ((big_b - 10) < b < (big_b + 10)) and (
                                    (big_c - 10) < c < (big_c + 10))):
                                found_pixel = found_pixel + 1
                print('{}'.format(found_pixel))
                if float(found_pixel) / float(total_pixel) > 0.12:
                    print('Succefull {}, {}'.format(screened_img_pixel_w, screened_img_pixel_h))
                    detected.rectangle((screened_img_pixel_w, screened_img_pixel_h, sprite_width + screened_img_pixel_w,
                                        sprite_height + screened_img_pixel_h), outline='red')
                    print(time.clock())
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    window.createWindow(screened_img)

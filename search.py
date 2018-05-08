import cv2
import numpy as np
import time


def search(screened_img):
    sprite_list = ['spr_main',
                   'spr_wait',
                   'spr_run_1',
                   'spr_run_2',
                   'spr_jump_1',
                   'spr_jump_2',
                   'spr_fail_1',
                   'spr_fail_2'
                   ]
    sprite_list_bad = ['bug',
                       'bug2',
                       'crab',
                       'fish',
                       'fly',
                       'fly2',
                       'fly3',
                       'fly4'
                       ]

    sprites = []
    sprites_bad = []
    for spr in sprite_list:
        screen = cv2.imread('Images/Sonic/{}.jpg'.format(spr))
        sprites.append(cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY))
    for spr in sprite_list_bad:
        screen = cv2.imread('Images/Badboys/{}.jpg'.format(spr))
        sprites_bad.append(cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY))

    tm = time.time()
    threshold = 0.5
    for sprite in sprites:
        sprite_width, sprite_height = sprite.shape[::-1]
        result = cv2.matchTemplate(screened_img, sprite, cv2.TM_CCOEFF_NORMED)

        location = np.where(result >= threshold)
        print("Detected in {} seconds".format(round(time.time() - tm, 3)))
        if len(location[0]) > 0:
            for pt in zip(*location[::-1]):
                cv2.rectangle(screened_img, pt, (pt[0] + sprite_width, pt[1] + sprite_height), 0, 2)
            break
    for sprite in sprites_bad:
        sprite_width_bad, sprite_height_bad = sprite.shape[::-1]
        result = cv2.matchTemplate(screened_img, sprite, cv2.TM_CCOEFF_NORMED)
        location_bad = np.where(result >= threshold)
        if len(location_bad[0]) > 0:
            for pt in zip(*location_bad[::-1]):
                cv2.rectangle(screened_img, pt, (pt[0] + sprite_width_bad, pt[1] + sprite_height_bad), 255, 2)

    return screened_img

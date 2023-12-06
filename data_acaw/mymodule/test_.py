import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_acaw import imgs_set_
    from dead_die import boohwal
    from action import out_check
    from potion import buy_potion, maul_move_check, soongan_move_check, my_potion_check
    from get_item import set_collection, boonhae, get_post, daily_check


    print("test")
    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3

    my_potion_check(cla)

    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\list_have_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(160, 320, 210, 360, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("list_have_1, 아이템", imgs_)
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

    from function_acaw import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from dead_die import boohwal
    from action import out_check, clean_screen, juljun_off, juljun_on, auto_on, bag_open
    from potion import buy_potion, maul_move_check, soongan_move_check, my_potion_check, juljun_potion_checking, chango_in
    from get_item import set_collection, boonhae, get_post, daily_check, get_sohwan
    from jadong_acaw import jadong_in_spot_go, jadong_start
    from sub_quest_acaw import request_complete_check

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

    # for i in range(15):
    #     full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\worldmap_up.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(200, 100, 280, 1040, cla, img, 0.7)
    #     if imgs_ is not None and imgs_ != False:
    #         print("worldmap_up", imgs_)
    #         click_pos_reg(imgs_.x, imgs_.y, cla)
    #     else:
    #         break
    #     time.sleep(0.5)

    # jadong_start(cla, "자동_송별의뜰")

    # buy_potion(cla)


    # boonhae(cla)


    # 의뢰 완료
    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\sohwan_1.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(200, 130, 500, 840, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("sohwan_1", imgs_)

    # request_complete_check(cla)


    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\out_small_potion.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(460, 950, 500, 1005, cla, img, 0.6)
    # if imgs_ is not None and imgs_ != False:
    #     v_.my_potion_check = 0
    #     print("out_small_potion", imgs_)
    # else:
    #     full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\out_middle_potion.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(460, 950, 500, 1005, cla, img, 0.6)
    #     if imgs_ is not None and imgs_ != False:
    #         v_.my_potion_check = 0
    #         print("out_middle_potion", imgs_)
    #     else:
    #         v_.my_potion_check += 1
    #         print("포션 없다", v_.my_potion_check)
    #
    #         juljun_potion_checking(cla)
    #
    #         if v_.my_potion_check > 3:
    #             buy_potion(cla)
    #
    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\time_out.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(650, 630, 740, 690, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("time_out", imgs_)
    #
    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\time_out_test.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(650, 630, 740, 690, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("time_out_test", imgs_)

    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\my_maul_move_sangjum.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(690, 150, 940, 950, cla, img, 0.6)
    # if imgs_ is not None and imgs_ != False:
    #     print("my_maul_move_sangjum", imgs_)
    #
    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\my_random_move_sangjum.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(690, 150, 940, 950, cla, img, 0.6)
    # if imgs_ is not None and imgs_ != False:
    #     print("my_random_move_sangjum", imgs_)
    #
    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\juljun_small_potion_zero.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(400, 950, 600, 1030, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("juljun_small_potion_zero", imgs_)
    #
    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\juljun_middle_potion_zero.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(400, 950, 600, 1030, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("juljun_middle_potion_zero", imgs_)

    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\auto_on.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(850, 900, 940, 940, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("auto_on", imgs_)
    #
    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\auto_off.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(850, 900, 940, 940, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("auto_off", imgs_)
    #
    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\out_small_potion.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(460, 950, 500, 1005, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("out_small_potion", imgs_)
    #
    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\out_middle_potion.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(460, 950, 500, 1005, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("out_middle_potion", imgs_)

    # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\list_have_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(160, 320, 210, 360, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("list_have_1, 아이템", imgs_)
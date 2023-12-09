import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

import time
import pyautogui



def tuto_start(cla, data):
    try:
        from potion import my_potion_check
        from dead_die import dead_die_start

        #포션체크
        #my_potion_check(cla)
        dead_die_start(cla, data)
        #설명하는 것들
        print("설명하는 것들")
        tuto_first(cla)
        tuto_quest_moglog(cla)
        tuto_bag_touch(cla)
        tuto_camera_setting(cla)
        tuto_new_skill(cla)
        tuto_talgut(cla)
        tuto_sangjum(cla)
        tuto_groa(cla)

        # 확인
        print("일반적인 함수")
        tuto_confirm(cla)
        go_quest_ing(cla)
        quest_clear_click(cla)
        tuto_skip(cla)
        tuto_status(cla)


    except Exception as e:
        print(e)
        return 0



def tuto_confirm(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 930, 860, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\confirm_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 600, 630, 650, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("confirm_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)
        return 0


def go_quest_ing(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        from action import out_check


        ing_ = False
        ing_count = 0
        while ing_ is False:
            ing_count += 1
            if ing_count > 5:
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\confirm_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(470, 590, 660, 660, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    ing_ = True
                    print("confirm_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(3)
                    out_ = False
                    out_count = 0
                    while out_ is False:
                        out_count += 1
                        if out_count > 30:
                            out_ = True
                        result_out = out_check(cla)
                        if result_out == True:
                            click_pos_2(800, 100, cla)
                            out_ = True
                        time.sleep(0.2)
                    time.sleep(3)
                if ing_count > 20:
                    ing_ = True
                    print("무언가 잘못 되었다.")
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\go_quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(640, 70, 690, 120, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("go_quest", imgs_)
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\check\\lv_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(47, 30, 70, 50, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("lv_point", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
                    click_pos_2(195, 990, cla)
                    tuto_status(cla)
                ing_ = True
            else:
                if ing_count < 2:
                    click_pos_2(905, 90, cla)
                if 12 < ing_count < 14:
                    click_pos_2(800, 100, cla)
                    ing_ = True
            time.sleep(0.3)

    except Exception as e:
        print(e)
        return 0

# def go_quest_ing(cla):
#     try:
#         import cv2
#         import numpy as np
#         from function_acaw import click_pos_reg, imgs_set_, click_pos_2
#
#         ing_ = False
#         ing_count = 0
#         while ing_ is False:
#             ing_count += 1
#             if ing_count > 10:
#                 full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\confirm_2.PNG"
#                 img_array = np.fromfile(full_path, np.uint8)
#                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                 imgs_ = imgs_set_(470, 590, 660, 660, cla, img, 0.8)
#                 if imgs_ is not None and imgs_ != False:
#                     ing_ = True
#                     print("confirm_1", imgs_)
#                     click_pos_reg(imgs_.x, imgs_.y, cla)
#                 else:
#                     if ing_count < 12:
#                         click_pos_2(905, 90, cla)
#                 if ing_count > 20:
#                     ing_ = True
#                     print("무언가 잘못 되었다.")
#             full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\go_quest.PNG"
#             img_array = np.fromfile(full_path, np.uint8)
#             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#             imgs_ = imgs_set_(640, 70, 690, 120, cla, img, 0.8)
#             if imgs_ is not None and imgs_ != False:
#                 print("go_quest", imgs_)
#                 ing_ = True
#             else:
#                 if ing_count < 2:
#                     click_pos_2(800, 100, cla)
#             time.sleep(0.3)
#
#     except Exception as e:
#         print(e)
#         return 0

def quest_clear_click(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\quest_clear_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(640, 70, 690, 120, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("go_quest", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
    except Exception as e:
        print(e)
        return 0



def tuto_skip(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(690, 870, 960, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("skip_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\skip_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 120, 960, 400, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("skip_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)
        return 0

def tuto_status(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2, drag_pos
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_status_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 80, 70, 130, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_status_1", imgs_)
            is_stat_ = False
            is_stat_count = 0
            while is_stat_ is False:
                is_stat_count += 1
                if is_stat_count > 5:
                    is_stat_ = True
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_status_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 135, 80, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(480, 685, cla)
                    time.sleep(0.1)
                    click_pos_2(255, 110, cla)
                    is_stat_ = True
                else:
                    click_pos_2(480, 515, cla)
                    time.sleep(0.1)
                    click_pos_2(480, 515, cla)
                    time.sleep(0.1)
                    click_pos_2(480, 515, cla)
                    time.sleep(0.1)
                    drag_pos(400, 640, 400, 300, cla)
                    time.sleep(0.1)
                    click_pos_2(480, 430, cla)
                    time.sleep(0.1)
                    click_pos_2(480, 430, cla)
                    time.sleep(0.1)
                time.sleep(0.1)


    except Exception as e:
        print(e)
        return 0

######################### 튜 토 리 얼 #########################################################

def tuto_first(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_first_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 300, 560, 350, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_quest_moglog_1", imgs_)
            click_pos_2(505, 270, cla)
        else:
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_attack_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(550, 880, 670, 970, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("tuto_attack_1", imgs_)
                click_pos_2(865, 920, cla)
                time.sleep(1)
                for i in range(10):
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_first_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 300, 560, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(865, 920, cla)
                    time.sleep(1)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_setting_touch.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 300, 760, 650, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_setting_touch", imgs_)
            click_pos_2(820, 380, cla)

    except Exception as e:
        print(e)
        return 0

def tuto_quest_moglog(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_quest_moglog_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(630, 150, 900, 260, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_quest_moglog_1", imgs_)
            click_pos_2(800, 100, cla)

    except Exception as e:
        print(e)
        return 0

def tuto_bag_touch(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2, drag_pos
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(630, 150, 900, 260, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_1", imgs_)
            click_pos_2(770, 55, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(420, 360, 535, 435, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_2", imgs_)
            click_pos_2(730, 385, cla)
            time.sleep(0.1)
            click_pos_2(730, 385, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 555, 455, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_3", imgs_)
            click_pos_2(730, 385, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 820, 630, 900, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_4", imgs_)
            click_pos_2(530, 980, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 820, 660, 920, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_5", imgs_)
            drag_pos(530, 965, 530, 995, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 380, 780, 430, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_6", imgs_)
            click_pos_2(915, 340, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_7.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(465, 860, 580, 920, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_7", imgs_)
            click_pos_2(480, 980, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_8.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 100, 920, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_8", imgs_)
            click_pos_2(900, 55, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_9.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(540, 300, 700, 350, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_9", imgs_)
            click_pos_2(820, 330, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_10.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(370, 170, 540, 240, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_10", imgs_)
            click_pos_2(200, 100, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_11.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(670, 350, 820, 420, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_11", imgs_)
            click_pos_2(750, 200, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_bag_touch_12.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(740, 140, 890, 190, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_bag_touch_12", imgs_)
            click_pos_2(915, 55, cla)


    except Exception as e:
        print(e)
        return 0


def tuto_camera_setting(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\camera_setting_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(250, 920, 400, 960, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("camera_setting_1", imgs_)
            click_pos_2(40, 955, cla)

    except Exception as e:
        print(e)
        return 0

def tuto_new_skill(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2, drag_pos
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_new_skill_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(720, 160, 840, 220, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_new_skill", imgs_)
            click_pos_2(770, 60, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_new_skill_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 370, 540, 420, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_new_skill", imgs_)
            click_pos_2(730, 390, cla)
            time.sleep(0.1)
            click_pos_2(730, 390, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_new_skill_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(770, 170, 870, 220, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_new_skill", imgs_)
            click_pos_2(810, 60, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_new_skill_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(690, 480, 840, 540, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_new_skill", imgs_)
            click_pos_2(725, 385, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_new_skill_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(160, 830, 350, 870, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_new_skill", imgs_)
            click_pos_2(200, 980, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_new_skill_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(210, 830, 350, 870, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_new_skill", imgs_)
            drag_pos(200, 965, 200, 990, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_new_skill_7.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(210, 830, 350, 870, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_new_skill", imgs_)
            click_pos_2(815, 685, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_new_skill_8.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(740, 440, 790, 490, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_new_skill", imgs_)
            click_pos_2(915, 340, cla)

    except Exception as e:
        print(e)
        return 0

def tuto_talgut(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(720, 160, 825, 210, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_1", imgs_)
            click_pos_2(775, 60, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(670, 470, 740, 550, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_2", imgs_)
            click_pos_2(730, 390, cla)
            time.sleep(0.1)
            click_pos_2(730, 390, cla)
        #중복
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 930, 600, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_3", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            pyautogui.moveTo(imgs_.x + 100, imgs_.y)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 930, 600, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_4", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        #
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(720, 135, 860, 180, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_5", imgs_)
            click_pos_2(900, 60, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(710, 160, 810, 210, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_6", imgs_)
            click_pos_2(815, 110, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_7.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(740, 890, 835, 945, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_7", imgs_)
            click_pos_2(860, 990, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_8.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 940, 720, 990, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_8", imgs_)
            click_pos_2(900, 980, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_9.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 480, 815, 565, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_9", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0

def tuto_sangjum(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_sangjum_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 160, 800, 220, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_sangjum_1", imgs_)
            click_pos_2(730, 55, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_sangjum_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(530, 240, 670, 290, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_sangjum_2", imgs_)
            click_pos_2(250, 245, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_sangjum_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(690, 570, 850, 640, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_sangjum_3", imgs_)
            click_pos_2(560, 700, cla)

        # 중복
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 930, 600, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_3", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            pyautogui.moveTo(imgs_.x + 100, imgs_.y)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 930, 600, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_4", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        #

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_sangjum_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(740, 130, 890, 180, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_sangjum_4", imgs_)
            click_pos_2(915, 55, cla)

    except Exception as e:
        print(e)
        return 0


def tuto_groa(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        from schedule import myQuest_play_add
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_groa_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(720, 190, 840, 240, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_groa_1", imgs_)
            click_pos_2(770, 55, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_groa_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 480, 800, 550, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_groa_2", imgs_)
            click_pos_2(730, 390, cla)
            time.sleep(0.1)
            click_pos_2(730, 390, cla)

        # 중복
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 930, 600, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_3", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            pyautogui.moveTo(imgs_.x + 100, imgs_.y)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_talgut_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 930, 600, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_talgut_4", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        #

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_groa_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(730, 140, 860, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_groa_3", imgs_)
            click_pos_2(900, 55, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_groa_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 200, 800, 250, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_groa_4", imgs_)
            click_pos_2(770, 110, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_groa_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(745, 890, 865, 945, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_groa_5", imgs_)
            click_pos_2(865, 990, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\tuto_groa_6.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 480, 790, 540, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_groa_6", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

            print("튜툐 끝?")
            # myQuest_play_add(cla, "튜토육성")


    except Exception as e:
        print(e)
        return 0

# def tuto_box_open(cla):
#     try:
#         import cv2
#         import numpy as np
#         from function_acaw import click_pos_reg, imgs_set_, click_pos_2
#         full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\box\\moogi_select_box_1.PNG"
#         img_array = np.fromfile(full_path, np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         imgs_ = imgs_set_(680, 320, 950, 670, cla, img, 0.8)
#         if imgs_ is not None and imgs_ != False:
#             print("moogi_select_box_1", imgs_)
#             click_pos_reg(imgs_.x, imgs_.y, cla)
#             time.sleep(0.1)
#             click_pos_reg(imgs_.x, imgs_.y, cla)
#             time.sleep(1)
#             from function_acaw import click_pos_reg, imgs_set_, click_pos_2
#             full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\box\\moogi_select_box_2.PNG"
#             img_array = np.fromfile(full_path, np.uint8)
#             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#             imgs_ = imgs_set_(500, 500, 600, 600, cla, img, 0.8)
#             if imgs_ is not None and imgs_ != False:
#                 print("moogi_select_box_2", imgs_)
#                 click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0




import sys
import time

import pyautogui

sys.path.append('C:/acaw/my_acaw/mymodule')

import variable as v_


def common_start(cla, data):
    try:
        from potion import my_potion_check
        from dead_die import dead_die_start

        #포션체크
        my_potion_check(cla)
        dead_die_start(cla, data)

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
        from potion import my_potion_check


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
                    time.sleep(2)
                    out_ = False
                    out_count = 0
                    while out_ is False:
                        out_count += 1
                        if out_count > 30:
                            out_ = True
                        result_out = out_check(cla)
                        if result_out == True:
                            my_potion_check(cla)
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
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
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
                if is_stat_count > 10:
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

    except Exception as e:
        print(e)
        return 0

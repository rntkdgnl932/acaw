import sys
import time

import pyautogui

sys.path.append('C:/acaw/my_acaw/mymodule')

import variable as v_


def sowon_start(cla):
    import cv2
    import numpy as np
    from function_acaw import click_pos_reg, imgs_set_, click_pos_2
    try:


        print("sowon_start")

        is_water = True

        while is_water is True:
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sowon\\gogb_rare.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(70, 125, 155, 500, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("gogb_rare", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
                click_pos_2(840, 1005, cla)

                for i in range(20):
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sowon\\not_water.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 450, 630, 530, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("not_water", imgs_)
                        is_water = False
                        break
                    else:
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sowon\\bag_full.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 140, 600, 200, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("bag_full", imgs_)
                            is_water = False
                            break

                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sowon\\screen_touch.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 850, 470, 930, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("not_water", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break

                    time.sleep(0.5)

            else:
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sowon\\refresh_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 970, 130, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("refresh_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sowon\\gogb_rare.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(70, 125, 155, 500, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sowon\\confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 620, 640, 670, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)

            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sowon\\screen_touch.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 850, 470, 930, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("not_water", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            time.sleep(1)



    except Exception as e:
        print(e)
        return 0


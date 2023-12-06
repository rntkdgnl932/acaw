import sys
import time

import pyautogui

sys.path.append('C:/acaw/my_acaw/mymodule')

import variable as v_


def jadong_start(cla, data):
    try:
        import numpy as np
        import cv2

        from dead_die import dead_die_start
        from potion import buy_potion, my_potion_check
        from function_acaw import click_pos_2, imgs_set_
        from action import out_check

        print("jadong")
        if v_.jadong_on == False:
            in_worldmap(cla)
            go_jadong(cla, data)



            go_auto(cla)
        else:
            result_in = in_spot_check(cla)
            print("result_in", result_in)
            print("v_.jadong_on_count", v_.jadong_on_count)
            if result_in == True:
                v_.jadong_on_count = 0

                my_potion_check(cla)
                dead_die_start(cla, data)
            else:
                v_.jadong_on_count += 1
                if v_.jadong_on_count > 5:
                    v_.jadong_on = False



    except Exception as e:
        print(e)
        return 0





def in_spot_check(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import imgs_set_

        in_spot_ = False
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_list_in\\common.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 70, 110, 110, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            in_spot_ = True
        else:
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_list_in\\common.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 70, 110, 110, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                in_spot_ = True

        return in_spot_
    except Exception as e:
        print(e)
        return 0

def in_worldmap(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        from action import clean_screen

        in_w_ = False
        in_w_count = 0
        while in_w_ is False:
            in_w_count += 1
            if in_w_count > 10:
                in_w_ = True
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\worldmap_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(790, 30, 900, 90, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(30, 180, cla)
                in_w_ = True
                print("worldmap_title", imgs_)
            else:
                clean_screen(cla)
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jabhwa_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 80, 300, 200, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("jabhwa_1", imgs_)
                    click_pos_2(40, 100, cla)
                else:
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jabhwa_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 80, 300, 200, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jabhwa_2", imgs_)
                        click_pos_2(40, 100, cla)
                time.sleep(0.3)
                click_pos_2(140, 140, cla)

    except Exception as e:
        print(e)
        return 0

def go_jadong(cla, data):
    try:
        import os
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        from action import out_check
        from potion import my_potion_check

        if "_" in data:
            spot_ = data.split("_")
        print("spot_", spot_)

        dir_path = "C:\\my_games\\acaw\\data_acaw"
        file_path = dir_path + "\\jadong\\jadong.txt"

        ja_li_ = False
        while ja_li_ is False:
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='UTF8') as file:
                    ja_li_ = True
                    read_list = file.read().splitlines()
                    print("read_list", read_list)
            else:
                with open(file_path, "w", encoding='UTF8') as file:
                    file.write("백월만/backwallman")
        for i in range(len(read_list)):
            result_spot = read_list[i].split("/")
            print("result_spot", result_spot)
            if spot_[1] == result_spot[0]:
                spot_name = result_spot[1]

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\worldmap_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(790, 30, 900, 90, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("worldmap_title", imgs_)

            jadong_hunt = False
            jadong_hunt_count = 0
            while jadong_hunt is False:
                jadong_hunt_count += 1
                if jadong_hunt_count > 10:
                    jadong_hunt = True

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_soongan_move.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 970, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("jadong_soongan_move", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    click_pos_2(30, 180, cla)
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_list\\" + spot_name + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(80, 120, 250, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print(spot_name, imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\confirm_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 610, 630, 660, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("confirm_1", imgs_)

                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    is_out = False
                    is_out_count = 0
                    while is_out is False:
                        is_out_count += 1
                        if is_out_count > 30:
                            is_out = True
                            jadong_hunt = True
                        result_out = out_check(cla)
                        if result_out == True:
                            jadong_hunt = True
                            my_potion_check(cla)
                        time.sleep(0.3)

        else:
            in_worldmap(cla)

    except Exception as e:
        print(e)
        return 0

def go_auto(cla):
    try:
        import numpy as np
        import cv2

        from function_acaw import click_pos_2, imgs_set_
        from potion import buy_potion
        from action import out_check, clean_screen

        print("go_auto")

        auto_ = False
        auto_count = 0
        while auto_ is False:
            auto_count += 1
            if auto_count > 10:
                auto_ = True
            result_out = out_check(cla)
            if result_out == True:
                v_.jadong_on = True
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\auto_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 900, 940, 940, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("auto_on", imgs_)
                    auto_ = True
                else:
                    print("auto_on이 아니다.")
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\auto_off.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(850, 900, 940, 940, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("auto_off", imgs_)
                        auto_ = True
                        click_pos_2(900, 935, cla)
                    else:
                        print("auto_off 아니다.")
            else:
                clean_screen(cla)
            time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0


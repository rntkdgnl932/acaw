import sys
import time

import pyautogui

sys.path.append('C:/acaw/my_acaw/mymodule')

import variable as v_


def get_item_start(cla):
    try:
        from action import clean_screen
        from schedule import myQuest_play_add
        print("get_item_start")
        get_post(cla)
        set_collection(cla)
        boonhae(cla)
        daily_check(cla)

        clean_screen(cla)

        myQuest_play_add(cla, "각종템받기")


    except Exception as e:
        print(e)
        return 0


def get_post(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_reg, imgs_set_, click_pos_2
        from action import clean_screen, menu_open, bag_open



        in_post = False
        in_post_count = 0
        while in_post is False:
            in_post_count += 1
            if in_post_count > 7:
                in_post = True
            # 우편 타이틀
            full_path = "c:\\acaw\\my_acaw\\imgs\\get_item\\post_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(820, 30, 900, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("post_title", imgs_)
                click_pos_2(860, 990, cla)
                time.sleep(0.3)
                full_path = "c:\\acaw\\my_acaw\\imgs\\get_item\\daily_confirm_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 600, 650, 650, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                click_pos_2(860, 990, cla)
                time.sleep(0.3)
                click_pos_2(915, 60, cla)
            else:
                menu_open(cla)
                time.sleep(0.2)

                # 우편 포인트
                full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(895, 180, 925, 210, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("우편 포인트 있다.", imgs_)
                    click_pos_reg(imgs_.x - 8, imgs_.y + 8, cla)
                else:
                    in_post = True
                    print("우편 포인트 없다.")
            time.sleep(0.3)

        clean_screen(cla)



    except Exception as e:
        print(e)
        return 0

def set_collection(cla):
    try:
        import os
        import cv2
        import numpy as np
        from function import click_pos_reg, imgs_set_, click_pos_2
        from action import menu_open, clean_screen



        in_collection = False
        in_collection_count = 0
        while in_collection is False:
            in_collection_count += 1
            if in_collection_count > 7:
                in_collection = True
            # 컬렉션 타이틀
            full_path = "c:\\acaw\\my_acaw\\imgs\\get_item\\collection_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 900, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("collection_title", imgs_)
                # 컬렉션 내부
                in_collection = True


                for i in range(5):
                    x_reg = 100 * i
                    full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(170 + x_reg, 80, 260 + x_reg, 110, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("위 컬렉션 포인트 있다.", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)

                        collection_start2 = False
                        collection_start_count2 = 0
                        while collection_start2 is False:
                            collection_start_count2 += 1
                            if collection_start_count2 > 3:
                                collection_start2 = True
                            full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 110, 680, 970, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("컬렉션 포인트 있다.", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)

                                get_ = False
                                get_count = 0
                                while get_ is False:
                                    get_count += 1
                                    if get_count > 3:
                                        get_ = True
                                    full_path = "c:\\acaw\\my_acaw\\imgs\\get_item\\daily_confirm_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 600, 650, 650, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        click_pos_2(890, 990, cla)
                                    time.sleep(0.3)
                            else:
                                collection_start2 = True
                            time.sleep(0.1)

                    else:
                        print("끝")
                    time.sleep(0.2)
            else:
                menu_open(cla)
                time.sleep(0.2)

                # 컬렉션 포인트
                full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 80, 880, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("컬렉션 포인트 있다.", imgs_)
                    click_pos_reg(imgs_.x - 8, imgs_.y + 8, cla)
                else:
                    print("컬렉션 포인트 없다.")
                    in_collection = True
            time.sleep(0.3)

        clean_screen(cla)




    except Exception as e:
        print(e)
        return 0

def daily_check(cla):
    try:
        import numpy as np
        import cv2

        from function import click_pos_2, imgs_set_, click_pos_reg
        from potion import buy_potion
        from action import out_check, clean_screen, menu_open

        print("daily_check")

        in_daily = False
        in_daily_count = 0
        while in_daily is False:
            in_daily_count += 1
            if in_daily_count > 7:
                in_daily = True
            # 출석 타이틀
            full_path = "c:\\acaw\\my_acaw\\imgs\\get_item\\daily_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 30, 840, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("출석 daily_title 있다.", imgs_)
                #출석 내부

                in_daily2 = False
                in_daily_count2 = 0
                while in_daily2 is False:
                    in_daily_count2 += 1
                    if in_daily_count2 > 7:
                        in_daily2 = True
                    full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(130, 80, 680, 110, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("데일리 포인트 있다.", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)

                        full_path = "c:\\acaw\\my_acaw\\imgs\\get_item\\get_daily_bosang.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 720, 880, 780, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            in_daily2 = True
                            click_pos_2(775, 755, cla)
                else:
                    print("끝")
                    in_daily = True
                time.sleep(0.2)
            else:
                menu_open(cla)
                time.sleep(0.2)

                # 출석 포인트
                full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(725, 180, 750, 210, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("출석 포인트 있다.", imgs_)
                    click_pos_reg(imgs_.x - 8, imgs_.y + 8, cla)
                else:
                    in_daily = True
                    print("출석 포인트 없다.")
            time.sleep(0.3)

        clean_screen(cla)

    except Exception as e:
        print(e)
        return 0

def boonhae(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_reg, imgs_set_, click_pos_2
        from action import clean_screen, menu_open, bag_open

        bag_open(cla)
        full_path = "c:\\acaw\\my_acaw\\imgs\\clean_screen\\bag_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 660, 750, 705, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("bag_1", imgs_)
            b_x_reg = imgs_.x
            b_y_reg = imgs_.y
            click_pos_reg(imgs_.x, imgs_.y, cla)
            boonhae_ready = False
            boonhae_ready_count = 0
            while boonhae_ready is False:
                boonhae_ready_count += 1
                if boonhae_ready_count > 3:
                    boonhae_ready = True
                full_path = "c:\\acaw\\my_acaw\\imgs\\get_item\\boonhae_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(690, 310, 760, 360, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("boonhae_title", imgs_)

                    full_path = "c:\\acaw\\my_acaw\\imgs\\get_item\\daily_confirm_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 600, 660, 660, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("daily_confirm_1", imgs_)
                        boonhae_ready = True
                    else:
                        click_pos_2(720, 650, cla)
                        time.sleep(0.2)
                        click_pos_2(820, 685, cla)

                else:
                    click_pos_reg(b_x_reg, b_y_reg, cla)



    except Exception as e:
        print(e)
        return 0



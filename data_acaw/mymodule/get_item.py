import sys
import time

import pyautogui

sys.path.append('C:/acaw/my_acaw/mymodule')

import variable as v_


def get_item_start(cla):

    from action import juljun_off

    try:
        from action import clean_screen
        print("get_item_start")

        juljun_off(cla)

        get_sohwan(cla)

        get_post(cla)
        set_collection(cla)
        boonhae(cla)
        daily_check(cla)

        clean_screen(cla)




    except Exception as e:
        print(e)
        return 0


def get_sohwan(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        from action import clean_screen, menu_open, bag_open



        in_sohwan = False
        in_sohwan_count = 0
        while in_sohwan is False:
            in_sohwan_count += 1
            if in_sohwan_count > 7:
                in_sohwan = True
            # 우편 타이틀
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_sangjum.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 930, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title_sangjum", imgs_)

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\gyohwanso_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(160, 70, 270, 130, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)

                    for i in range(5):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\sohwan_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 130, 500, 840, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\gyohwanso_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 120, 140, 340, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                        time.sleep(0.5)

                    for i in range(10):

                        is_sohwan = False

                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\sohwan_groa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 130, 500, 960, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            is_sohwan = True
                        else:
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\sohwan_job.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 130, 500, 960, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                is_sohwan = True
                            else:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\sohwan_talgut.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(200, 130, 500, 960, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    is_sohwan = True
                        if is_sohwan == True:
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\sohwan_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 660, 640, 710, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                for e in range(10):
                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\exit.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(330, 930, 660, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\bogi.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(330, 930, 660, 1030, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                        else:
                            in_sohwan = True

                else:
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\gyohwanso_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 120, 140, 340, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        for i in range(10):

                            is_sohwan = False

                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\sohwan_groa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 130, 500, 960, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                is_sohwan = True
                            else:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\sohwan_job.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(200, 130, 500, 960, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    is_sohwan = True
                                else:
                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\sohwan_talgut.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(200, 130, 500, 960, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        is_sohwan = True
                            if is_sohwan == True:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\sohwan_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 660, 640, 710, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                    for e in range(10):
                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\exit.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(330, 930, 660, 1030, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break
                                        else:
                                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\bogi.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(330, 930, 660, 1030, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.5)
                            else:
                                in_sohwan = True
                    else:
                        print("나타나지 않는 에러 발생")
                        in_sohwan = True
            else:
                menu_open(cla)
                time.sleep(0.2)

                # 상점가기

                for i in range(10):
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_sangjum.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 30, 930, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\menu_sangjum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 30, 760, 90, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_sangjum", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.3)
        for i in range(5):
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_sangjum.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 930, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(920, 60, cla)
            else:
                clean_screen(cla)
                break
            time.sleep(0.5)





    except Exception as e:
        print(e)
        return 0

def get_post(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        from action import clean_screen, menu_open, bag_open



        in_post = False
        in_post_count = 0
        while in_post is False:
            in_post_count += 1
            if in_post_count > 7:
                in_post = True
            # 우편 타이틀
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\post_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(820, 30, 900, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("post_title", imgs_)
                click_pos_2(860, 990, cla)
                time.sleep(0.3)
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\daily_confirm_1.PNG"
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
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\check\\point.PNG"
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
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        from action import menu_open, clean_screen



        in_collection = False
        in_collection_count = 0
        while in_collection is False:
            in_collection_count += 1
            if in_collection_count > 7:
                in_collection = True
            # 컬렉션 타이틀
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\collection_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 900, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("collection_title", imgs_)
                # 컬렉션 내부
                in_collection = True


                for i in range(5):
                    x_reg = 100 * i
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\check\\point.PNG"
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
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\check\\point.PNG"
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
                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\daily_confirm_1.PNG"
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
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\check\\point.PNG"
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

        from function_acaw import click_pos_2, imgs_set_, click_pos_reg
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
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\daily_title.PNG"
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
                    if in_daily_count2 > 10:
                        in_daily2 = True
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(130, 80, 680, 110, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("데일리 포인트 있다.", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)

                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\get_daily_bosang.PNG"
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
                    time.sleep(0.4)
            else:
                menu_open(cla)
                time.sleep(0.2)

                # 출석 포인트
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\check\\point.PNG"
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
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        from action import clean_screen, menu_open, bag_open

        bag_open(cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\bag_1.PNG"
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
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\boonhae_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(690, 310, 760, 360, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("boonhae_title", imgs_)

                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\daily_confirm_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 600, 660, 680, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("daily_confirm_1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        boonhae_ready = True
                        time.sleep(0.5)
                    else:
                        click_pos_2(720, 655, cla)
                        time.sleep(0.2)
                        click_pos_2(775, 655, cla)
                        time.sleep(0.2)
                        click_pos_2(820, 685, cla)
                        time.sleep(0.2)
                        for i in range(10):
                            ull_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\get_item\\daily_confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 600, 660, 680, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.2)


                else:
                    click_pos_reg(b_x_reg, b_y_reg, cla)



    except Exception as e:
        print(e)
        return 0



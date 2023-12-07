import sys
import time

import pyautogui

sys.path.append('C:/acaw/my_acaw/mymodule')

import variable as v_


def welcome_to_action(cla):
    try:

        print("this is action")



    except Exception as e:
        print(e)
        return 0


def clean_screen(cla):
    import cv2
    import numpy as np
    from function_acaw import click_pos_reg, imgs_set_, click_pos_2
    try:
        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

        clean_ = False
        clean_count = 0
        while clean_ is False:
            clean_count += 1
            if clean_count > 5:
                clean_ = True

            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\close_to_potion.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\close_to_potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                for i in pyautogui.locateAllOnScreen(img, region=(0 + plus, 30, 960, 1040), confidence=0.8):
                    last_x = i.left
                    last_y = i.top
                    print("last_x", last_x)
                    print("last_y", last_y)
                    click_pos_reg(last_x, last_y, cla)
                    time.sleep(0.3)


            result_out = out_check(cla)
            if result_out == True:
                clean_ = True
            else:
                # 일반적인 뒤로가기
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\back_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(880, 30, 960, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("back_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                # 가방 닫기
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\bag_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(690, 650, 750, 710, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("bag_1", imgs_)
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\close_to_potion.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(890, 300, 940, 370, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("close_to_potion", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                # 기술 닫기
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\skill.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(690, 650, 750, 710, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("bag_1", imgs_)
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\close_to_potion.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(890, 300, 940, 370, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("close_to_potion", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                # 메뉴 닫기
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\setting.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 300, 840, 410, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("setting", imgs_)
                    click_pos_2(900, 55, cla)
                # 커뮤니티 닫기
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\community.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 640, 260, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("community", imgs_)
                    click_pos_2(240, 340, cla)
                # 공간이동서 닫기
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\gongan_move.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 80, 130, 130, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("gongan_move", imgs_)
                    click_pos_2(255, 110, cla)
                # 건너뛰기 닫기
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\skip.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("skip", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                # 확인 닫기
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\skip2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("skip2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\confirm_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("confirm_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\confirm_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("confirm_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2

        go_ = False

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\check\\out_check_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(880, 30, 930, 80, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("out_check_1", imgs_)
            go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0

def menu_open(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\setting.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(790, 300, 840, 410, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("menu_opened")
        else:
            menu_check_ = False
            menu_check_count = 0
            while menu_check_ is False:
                menu_check_count += 1
                if menu_check_count > 7:
                    menu_check_ = True
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\check\\out_check_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(880, 30, 930, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("out_check_1", imgs_)

                    menu_check_2 = False
                    menu_check_count2 = 0
                    while menu_check_2 is False:
                        menu_check_count2 += 1
                        if menu_check_count2 > 7:
                            menu_check_2 = True
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 300, 840, 410, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("open_menu", imgs_)
                            menu_check_2 = True
                            menu_check_ = True
                        else:
                            click_pos_2(900, 55, cla)
                        time.sleep(0.5)
                else:
                    clean_screen(cla)


    except Exception as e:
        print(e)
        return 0

def bag_open(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2

        go_bag_ = False
        while go_bag_ is False:
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\bag_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 660, 750, 705, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bag_1", imgs_)
                go_bag_ = True
            else:
                clean_screen(cla)
                time.sleep(0.5)
                click_pos_2(770, 60, cla)
                time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0


def juljun_on(cla):
    import cv2
    import numpy as np
    from function_acaw import imgs_set_, click_pos_2, drag_pos
    try:

        juljun_ = False
        juljun_count = 0
        while juljun_ is False:
            juljun_count += 1
            if juljun_count > 7:
                juljun_ = True

            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\juljun\\juljun_ing.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 400, 600, 600, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("juljun_ing", imgs_)
                juljun_ = True
            else:
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_juljun.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 30, 900, 90, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    drag_pos(480, 480, 800, 480, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\juljun\\juljun_ing.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 400, 600, 600, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.2)

                else:
                    clean_screen(cla)
                    click_pos_2(45, 990, cla)
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0


def juljun_off(cla):
    import cv2
    import numpy as np
    from function_acaw import imgs_set_, drag_pos

    try:
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\juljun\\juljun_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 400, 600, 600, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:


            juljun_ = False
            juljun_count = 0
            while juljun_ is False:
                juljun_count += 1
                if juljun_count > 7:
                    juljun_ = True

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\juljun\\juljun_ing.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 400, 600, 600, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    drag_pos(480, 520, 800, 520, cla)
                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        juljun_ = True

                time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0

def auto_on(cla):
    import cv2
    import numpy as np
    from function_acaw import imgs_set_, click_pos_reg

    try:

        for i in range(10):

            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\auto_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(850, 900, 940, 940, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("auto_on", imgs_)
                break
            else:
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\auto_off.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 900, 940, 940, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("auto_off", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    clean_screen(cla)
            time.sleep(0.3)

    except Exception as e:
        print(e)
        return 0
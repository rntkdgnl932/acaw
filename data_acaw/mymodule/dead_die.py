import sys
import time

import pyautogui

sys.path.append('C:/acaw/my_acaw/mymodule')

import variable as v_


def dead_die_start(cla, data):
    try:
        from potion import buy_potion
        from schedule import myQuest_play_add

        print("dead_die")
        result_die = is_die(cla)
        if result_die == True:
            if data == "튜토육성":
                v_.tuto_die_count += 1
                print("v_.tuto_die_count", v_.tuto_die_count)
                if v_.tuto_die_count > 0:
                    myQuest_play_add(cla, data)
                boohwal(cla, data)
                buy_potion(cla)
            elif data == "의뢰퀘스트":
                myQuest_play_add(cla, data)

                boohwal(cla, data)
                buy_potion(cla)
            else:
                buy_potion(cla)
                boohwal(cla, data)




    except Exception as e:
        print(e)
        return 0


def is_die(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_

        die_ = False

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\maul_boohwal_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(365, 665, 580, 740, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("maul_boohwal_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            die_ = True

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\dead_penalty.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(365, 665, 580, 740, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dead_penalty", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            die_ = True

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\go_boohwal.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(260, 465, 700, 800, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("go_boohwal", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            die_ = True

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\boohwal_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(660, 30, 710, 80, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_1", imgs_)
            die_ = True
        else:
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\boohwal_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(660, 30, 710, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("boohwal_2", imgs_)
                die_ = True
            else:
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\boohwal_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(660, 30, 710, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("boohwal_3", imgs_)
                    die_ = True

        return die_
    except Exception as e:
        print(e)
        return 0

def boohwal(cla, data):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2
        from action import out_check, clean_screen
        from massenger import line_to_me
        from schedule import myQuest_play_add

        die_ = False

        # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\boohwal_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(660, 30, 710, 80, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("boohwal_1", imgs_)
        #     click_pos_reg(imgs_.x, imgs_.y, cla)
        #     die_ = True
        # else:
        #     full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\boohwal_2.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(660, 30, 710, 80, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         print("boohwal_2", imgs_)
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        #         die_ = True
        #     else:
        #         full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\boohwal_3.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(660, 30, 710, 80, cla, img, 0.8)
        #         if imgs_ is not None and imgs_ != False:
        #             print("boohwal_3", imgs_)
        #             click_pos_reg(imgs_.x, imgs_.y, cla)
        #             die_ = True

        # 진입
        for i in range(10):
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\list_ready_item.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(120, 320, 200, 360, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(65, 340, cla)
                die_ = True
                break
            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(650, 55, cla)
                else:
                    clean_screen(cla)
            time.sleep(1)

        if die_ == True:
            boohwal_after_1 = False
            boohwal_after_1_count = 0
            while boohwal_after_1 is False:
                boohwal_after_1_count += 1
                if boohwal_after_1_count > 10:
                    boohwal_after_1 = True
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\list_ready_item.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(120, 320, 200, 360, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("list_have_1, 아이템", imgs_)

                    boohwal_setting(cla)

                    if v_.no_more_boohwal == False:
                        boohwal_after_1 = True
                        boohwal_after_2 = False
                        boohwal_after_2_count = 0
                        while boohwal_after_2 is False:
                            boohwal_after_2_count += 1
                            if boohwal_after_2_count > 10:
                                boohwal_after_2 = True

                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\anymore_boggoo.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 470, 220, 540, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("anymore_boggoo, 경험치", imgs_)
                                boohwal_after_2 = True
                                click_pos_2(175, 335, cla)

                                if data == "튜토육성" or data == "일반육성":
                                    myQuest_play_add(cla, data)
                            else:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\confirm_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 610, 650, 670, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("confirm_1", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    click_pos_2(150, 390, cla)
                                    time.sleep(0.2)

                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\free_confirm_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(80, 650, 200, 710, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("free_confirm_1", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\not_free_confirm_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(80, 650, 200, 710, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("not_free_confirm_1", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)


                            time.sleep(0.5)
                    time.sleep(0.5)
                    boohwal_after_3 = False
                    boohwal_after_3_count = 0
                    while boohwal_after_3 is False:
                        boohwal_after_3_count += 1
                        if boohwal_after_3_count > 10:
                            boohwal_after_3 = True
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\anymore_boggoo.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 470, 220, 540, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("anymore_boggoo, 아이템", imgs_)
                            boohwal_after_3 = True
                            click_pos_2(240, 340, cla)

                        else:
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 610, 650, 670, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm_1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                click_pos_2(170, 340, cla)
                                time.sleep(0.3)

                                click_pos_2(150, 390, cla)
                                time.sleep(0.2)
                                click_pos_2(135, 680, cla)
                        time.sleep(0.5)
                time.sleep(0.3)

        return die_
    except Exception as e:
        print(e)
        return 0


def boohwal_setting(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2

        for i in range(10):
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dead_die\\dead_gold.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(100, 400, 700, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dead_gold", imgs_)
                break
            else:
               click_pos_2(240, 635, cla)
            time.sleep(0.3)


    except Exception as e:
        print(e)
        return 0
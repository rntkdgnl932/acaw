import sys
import time

import pyautogui

sys.path.append('C:/acaw/my_acaw/mymodule')

import variable as v_


def star_upgrade_start(cla):
    import cv2
    import numpy as np
    from function_acaw import click_pos_reg, imgs_set_, click_pos_2
    from action import menu_open
    from potion import buy_potion
    from schedule import myQuest_play_add
    try:


        print("star_upgrade_start")

        star_up_ = False
        star_up_count = 0
        while star_up_ is False:
            star_up_count += 1
            if star_up_count > 7:
                star_up_ = True

            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_star.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 900, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                star_up_ = True

                print("별자리")



                file_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\star\\star_list.txt"

                with open(file_path, "r", encoding='utf-8-sig') as file:
                    read_star = file.read().splitlines()
                    # print("read_star", read_star)
                for b in range(2):
                    for c in range(5):

                        is_star = False

                        for i in range(len(read_star)):
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\star\\" + str(read_star[i]) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(760, 310, 900, 370, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                is_star = True
                                print("어디?", read_star[i])
                                result_star = read_star[i].split("_")
                                print(result_star[0])
                                print(result_star[1])
                                break

                        if is_star == True:
                            file_path_2 = "C:\\my_games\\acaw\\data_acaw\\imgs\\star\\" + str(result_star[0]) + "\\" + str(result_star[1]) + ".txt"

                            with open(file_path_2, "r", encoding='utf-8-sig') as file:
                                read_star_2 = file.read().splitlines()

                            for i in range(len(read_star_2)):
                                result_click_reg = read_star_2[i].split(",")
                                x_reg = int(result_click_reg[0])
                                y_reg = int(result_click_reg[1])

                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\star\\star_complete.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(x_reg - 20, y_reg - 20, x_reg + 20, y_reg + 20, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("star_complete", imgs_)
                                else:
                                    click_pos_2(x_reg, y_reg, cla)
                                    for z in range(10):

                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\star\\akium.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(700, 800, 760, 930, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(860, 990, cla)
                                            break
                                        time.sleep(0.2)
                                    for z in range(10):

                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\star\\star_complete.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(x_reg - 20, y_reg - 20, x_reg + 20, y_reg + 20, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("star_complete", imgs_)
                                            break
                                        else:
                                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\star\\fail.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(360, 60, 760, 200, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_2(860, 990, cla)
                                            else:
                                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\star\\success.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(360, 60, 760, 200, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("success", imgs_)

                                                    for s in range(10):
                                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\star\\star_complete.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(x_reg - 20, y_reg - 20, x_reg + 20,
                                                                          y_reg + 20, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            break
                                                        time.sleep(0.5)

                                        time.sleep(0.5)
                        else:
                            # 신 -> 활자리

                            y_click = 130 + (c * 50)

                            click_pos_2(35, y_click, cla)
                            time.sleep(0.5)
                    if b == 1:
                        break

            else:
                menu_open(cla)
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\star\\menu_star.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 80, 935, 355, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_star.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 30, 900, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.2)





    except Exception as e:
        print(e)
        return 0



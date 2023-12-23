import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

request_go = False

def junjik_quest_start_ex(cla):
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("junjik_quest_start")
        # full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\18_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("18_1")
        #     click_pos_reg(imgs_.x, imgs_.y, cla)
        #     time.sleep(1)
        # full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\18_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("18_1")
        #     click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0

def junjik_quest_start(cla):
    global request_go
    import random
    import numpy as np
    import cv2
    from schedule import myQuest_play_add
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action import bag_open, menu_open, auto_on, out_check
    from potion import my_potion_check, buy_potion
    from dead_die import dead_die_start
    from tuto_acaw import tuto_skip

    try:
        print("junjik_quest_start")

        dead_die_start(cla, "전직퀘스트")

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\junjik\\junjik_ing_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(710, 950, 850, 990, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        if request_go == False:

            request_start = False
            request_start_count = 0
            while request_start is False:
                request_start_count += 1
                if request_start_count > 7:
                    request_start = True

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_quest.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(690, 30, 940, 670, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("quest")

                    click_pos_2(610, 105, cla)
                    time.sleep(0.1)
                    click_pos_2(610, 105, cla)
                    time.sleep(0.1)

                    not_have_request = False

                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\soongan_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(780, 960, 940, 1015, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            not_have_request = True
                        time.sleep(0.4)

                    if not_have_request == True:

                        request_start = True
                        # add 완료
                        myQuest_play_add(cla, "전직퀘스트")
                    else:
                        for i in range(10):
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\soongan_move_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 620, 640, 670, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                for o in range(10):
                                    result_out = out_check(cla)
                                    if result_out == True:
                                        request_start = True
                                        request_go = True
                                        break
                                    time.sleep(0.5)


                                break
                            else:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\soongan_move.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(780, 960, 940, 1015, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)
                            time.sleep(0.5)

                else:
                    menu_open(cla)
                    click_pos_2(860, 60, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_quest.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(690, 30, 940, 670, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.2)
        else:
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\go_quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(640, 70, 690, 290, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("junjik_quest", imgs_)
                my_potion_check(cla)
                auto_on(cla)
            else:
                request_go = False
                for i in range(10):
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\go_quest.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 70, 690, 290, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        request_go = True
                        break
                    else:
                        tuto_skip(cla)
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\junjik\\junjik_ing_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(710, 950, 850, 990, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                    time.sleep(0.3)


    except Exception as e:
        print(e)
        return 0




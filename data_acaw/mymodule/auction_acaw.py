import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def auction_start(cla):
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("auction_start")
        # 거래소 열고 판매등록 대기까지
        auction_open(cla)
        # 리스트 불러와서 판매시작
        auction_open(cla)


    except Exception as e:
        print(e)
        return 0

def auction_open(cla):
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2, text_check_get, in_number_check, int_put_
    from schedule import myQuest_play_add
    from action import menu_open

    try:
        print("auction_open")


        auction_in = False
        auction_in_count = 0
        while auction_in is False:
            auction_in_count += 1
            if auction_in_count > 7:
                auction_in = True
            full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\title\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 30, 900, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\auction\\auction_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(570, 120, 650, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("auction_ready", imgs_)
                    auction_in = True
                else:
                    click_pos_2(205, 105, cla)
                    time.sleep(0.5)

                auction_in = True
                print("거래소 오픈")




            else:
                menu_open(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\title\\auction_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(760, 30, 900, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\auction\\menu_auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 130, 940, 200, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.3)
                    time.sleep(0.7)


    except Exception as e:
        print(e)
        return 0

def auction_list(cla):
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2, text_check_get, in_number_check, int_put_
    from schedule import myQuest_play_add
    from action import menu_open

    try:
        print("auction_list")

        dir_path = "C:\\my_games\\" + str(v_.game_folder) + "//" + str(v_.data_folder)
        file_path = dir_path + "\\imgs\\auction\\list.txt"

        with open(file_path, "r", encoding='utf-8-sig') as file:
            read_list = file.read().splitlines()
            print("read_list", read_list)

        for i in range(len(read_list)):
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\auction\\list\\" + read_list[i] + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(670, 150, 950, 500, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print(read_list[i], imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                for s in range(10):
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\auction\\sell_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 290, 550, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)


    except Exception as e:
        print(e)
        return 0
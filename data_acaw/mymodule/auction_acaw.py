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
        print("_stop_please")
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\auction\\skip1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(540, 590, 630, 630, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("skip1")
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\auction\\skip_confrim.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 610, 640, 660, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("skip_confrim")
            click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0



